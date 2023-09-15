"""Max Heap implemented using an array"""
from __future__ import annotations
__author__ = "Brendon Taylor, modified by Jackson Goerner"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class MaxHeap(Generic[T]):
    """
    MaxHeap Implementation.

    Constants:
        MIN_MATERIALS {int} -- The minimum capacity is 1.

    Unless specified, all functions have time complexity of O(1).
    """
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        """
        Initialises an empty Max Heap
        
        Arguments:
            max_size (int): maximum size of the heap
        """
        self.length = 0
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap

        Returns:
            int: the number of elements in the heap
        """
        return self.length

    def is_full(self) -> bool:
        """
        Checks if the heap is full

        Returns:
            bool: True if the heap is full, False otherwise
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position

        Arguments:
            k (int): index of the element to rise

        Precondition:
            1 <= k <= self.length

        Time Complexity Analysis:
            Best Case: O(log n)
            Worst Case: O(log n)
        """
        item = self.the_array[k]
        while k > 1 and item > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising

        Arguments:
            element (T): element to add to the heap

        Precondition:
            not self.is_full()

        Returns:
            bool: True if the element was added, False otherwise
        
        Time Complexity Analysis:
            Best Case: O(log n)
            Worst Case: O(log n)
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.

        Arguments:
            k (int): index of the element to find the largest child of

        Precondition:
            1 <= k <= self.length // 2

        Returns:
            int: index of the largest child of k
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ 
        Make the element at index k sink to the correct position.

        Arguments:
            k (int): index of the element to sink

        Precondition:
            1 <= k <= self.length

        Time Complexity Analysis:
            Best Case: O(log n)
            Worst Case: O(log n)
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child] <= item:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item
        
    def get_max(self) -> T:
        """ 
        Remove (and return) the maximum element from the heap.
        
        Precondition:
            self.length > 0

        Returns:
            T: the maximum element in the heap

        Time Complexity Analysis:
            Best Case: O(log n)
            Worst Case: O(log n)
        """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt