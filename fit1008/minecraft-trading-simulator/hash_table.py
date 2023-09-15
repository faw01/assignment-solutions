""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
"""
from __future__ import annotations
__author__ = 'Brendon Taylor. Modified by Graeme Gange, Alexey Ignatiev, Jackson Goerner and Walmart Mojang'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from primes import LargestPrimeIterator
from referential_array import ArrayR
from typing import TypeVar, Generic
T = TypeVar('T')

class LinearProbeTable(Generic[T]):
    """
    Linear Probe Table.

    Attributes:
        tablesize {int} -- The size of the hash table
        count {int} -- The number of elements in the hash table
        table {ArrayR} -- The hash table
        conflicts_count {int} -- The number of conflicts in the hash table
        probe_total {int} -- The total number of probes
        probe_max {int} -- The maximum probe chain length
        rehash_count {int} -- The number of rehashes performed
        
    Unless specified, all functions have time complexity of O(1).
    """

    def __init__(self, expected_size: int, tablesize_override: int = -1) -> None:
        """
        Initialise the hash table.

        Arguments:
            expected_size {int} -- The expected size of the hash table
            tablesize_override {int} -- The size of the hash table. If -1, the size is calculated automatically
        """
        if tablesize_override == -1:
            self.override = False
            prime_iter = iter(LargestPrimeIterator(expected_size * 2, 2))  # Load factor of 0.5.
            self.tablesize = next(prime_iter)

        else:
            self.override = True
            self.tablesize = tablesize_override

        self.conflicts_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0
        self.count = 0
        self.table = ArrayR(self.tablesize)

    def hash(self, key: str) -> int:
        """
        Hash a key for insertion into the hashtable.

        Arguments:
            key {str} -- The key to hash

        Returns:
            int -- The hashed key

        Time Complexity Analysis:
            Best Case: O(1) - The key is in the first position
            Worst Case: O(K + N) - The key is not in the hash table
        """
        hash_value = 0
        for char in key:
            hash_value = (31 * hash_value + ord(char)) % len(self.table)
        return hash_value

    def statistics(self) -> tuple:
        """
        Returns a tuple of statistics about the hash table

        Returns:
            tuple -- A tuple of statistics about the hash table containing the following:
                - Number of conflicts in the hash table
                - Total number of probes
                - Maximum probe chain length
                - Number of rehashes performed      
        """
        return (self.conflicts_count, self.probe_total, self.probe_max, self.rehash_count)

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table

        Returns:
            int -- Number of elements in the hash table
        """
        return self.count

    def _linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        
        Arguments:
            key {str} -- The key to find the position for
            is_insert {bool} -- True if the key is being inserted, False otherwise

        Returns:
            int -- The position of the key in the hash table

        Precondition:
            KeyError is raised if the key is not in the hash table

        Time Complexity Analysis:
            Best Case: O(1) - The key is in the first position
            Worst Case: O(K + N) - The key is not in the hash table
        """

        position = self.hash(key)  # get the position using hash

        if is_insert and self.is_full():
            raise KeyError(key)

        # Initialise counter-variable to count the length of a probe-chain
        probe_chain_length = 0

        # If there is a conflict, increase conflict count
        # Conflict : Occurs when probing, if key has conflict, then increase conflict_count by 1.from
        # If the key-value at the position is not the same as the key, and if the hash returns
        # a position that is filled in the table, there is a conflict for the key.
        if self.table[position] is not None and self.table[position][0] != key:
            self.conflicts_count += 1


        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    self.probe_max = max(probe_chain_length, self.probe_max)
                    return position
                else:
                    self.probe_max = max(probe_chain_length, self.probe_max)
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                self.probe_max = max(probe_chain_length, self.probe_max)
                return position
            else:  # there is something but not the key, try next
                position = (position + 1) % len(self.table)

                # Increment probe chain length and probe total (distance) by 1 because
                #
                probe_chain_length += 1
                self.probe_total += 1

        self.probe_max = max(probe_chain_length, self.probe_max)
        raise KeyError(key)

    def keys(self) -> list[str]:
        """
        Returns all keys in the hash table.

        Returns:
            list[str]: A list of all keys in the hash table

        Time Complexity Analysis:
            Best Case: O(N) - The hash table is full
            Worst Case: O(N) - The hash table is full
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][0])
        return res

    def values(self) -> list[T]:
        """
        Returns all values in the hash table.

        Returns:
            list[T]: A list of all values in the hash table

        Time Complexity Analysis:
            Best Case: O(N) - The hash table is full
            Worst Case: O(N) - The hash table is full
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][1])
        return res

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        Arguments:
            key {str} -- The key to check

        Precondition:
            KeyError is raised if the key is not in the hash table

        Returns:
            bool -- True if the key is in the hash table, False otherwise

        Time Complexity Analysis:
            Best Case: O(1) - The key is in the first position
            Worst Case: O(K + N) - The key is not in the hash table
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key

        Arguments:
            key {str} -- The key to get the item at
        
        Returns:
            T -- The item at the key

        Precondition:
            KeyError is raised if the key is not in the hash table
        :see: #self._linear_probe(key: str, is_insert: bool)

        Time Complexity Analysis:
            Best Case: O(1) - The key is in the first position
            Worst Case: O(K + N) - The key is not in the hash table
        """
        position = self._linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table

        Arguments:
            key {str} -- The key to be inserted
            data {T} -- The data to be inserted

        Precondition:
            KeyError: When the key already exists in the hash table

        :see: #self._linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        # Check if must rehash before inserting key
        if self._must_rehash():
            self._rehash()

        position = self._linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1

        self.table[position] = (key, data)
        # self.insert(key, data)

    def is_empty(self):
        """
        Check if the hash table is empty

        Returns:
            bool: True if empty, False otherwise
        """
        return self.count == 0

    def is_full(self) -> bool:
        """
        Checks if the hash table is full

        Returns:
            bool -- True if the hash table is full, False otherwise
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call setitem method
            :see: #__setitem__(self, key: str, data: T)

        Arguments:
            key {str} -- Key to insert
            data {T} -- Data to insert

        Time Complexity Analysis:
            Best case: O(1) when the key is not in the hash table and the position is empty.
            Worst case: O(K + N) when the key is not in the hash table and the position is not empty.
        """
        # According to test_hash_table.py, rehash should be checked BEFORE inserting the item
        if self._must_rehash():
            self._rehash()

        self[key] = data

    def _must_rehash(self) -> bool:
        """
        Checks if N/M is more than the load factor defined as 0.5, where N is the number of elements and
        M is the number of spaces in ArrayR.

        Returns:
            bool -- True if need to rehash, False otherwise.
        """
        load_factor = 0.5
        num_of_elements = self.count
        array_spaces = len(self.table)

        return load_factor < (num_of_elements/array_spaces)

    def _rehash(self) -> None:
        """
        Resizes table accordinigly and reinserts all values

        Time Complexity Analysis:
            Best Case: O(N) where N is the number of elements in the hash table.
            Worst Case: O(N) where N is the number of elements in the hash table.
        """

        # Increment rehash_count whenever _rehash is called.
        self.rehash_count += 1

        temp = self.table # temporary variable to store current hashtable 
        new_rehash = LinearProbeTable(self.tablesize, -1) # declare new hashtable 
        self.table_size = new_rehash.tablesize

        old_table_count = self.count

        for i in temp: 
            if i is not None:
                new_rehash[i[0]] = i[1]
                # new_rehash.insert(i[0],i[1]) # insert element from old hashtable to new hashtable 
                
        self.count = new_rehash.count
        self.table = new_rehash.table

    def __str__(self) -> str:
        """
        Returns a string representation of the hash table by returning
        all they key/value pairs in the hash table.

        Returns:
            str -- A string representation of the hash table.
        
        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

class LinearProbeTableAnalysis(LinearProbeTable):

    def __init__(self, expected_size: int, tablesize_override: int = -1) -> None:
        super().__init__(expected_size, tablesize_override)
        self.hash_value = 0

    def set_hash_value(self, hash_value: int) -> None:
        self.hash_value = hash_value
    
    def hash(self, key: str) -> int:
        hash_value = self.hash_value
        for char in key:
            hash_value = (31 * hash_value + ord(char)) % len(self.table)
        return hash_value