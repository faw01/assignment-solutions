""""""

from __future__ import annotations
from tokenize import Triple

__author__ = ''
__docformat__ = 'reStructuredText'

class LargestPrimeIterator():
    """
    Generates prime numbers using the Sieve of Eratosthenes algorithm.

    Attributes:
        upper_bound {int} -- The upper bound of the iterator.
        factor {int} -- The factor of the iterator.

    Unless specified, all functions have time complexity of O(1).
    """

    def __init__(self, upper_bound: int, factor: int) -> None:
        """
        Initialises a LargestPrimeIterator object.
        
        Arguments:
            upper_bound {int} -- The upper bound of the iterator.
            factor {int} -- The factor of the iterator.
                    
        Precondition:
            upper_bound >= 2
            factor >= 2
        """
        if upper_bound < 2:
            raise AssertionError("The upper bound must be greater than or equal to 2.")
        if factor < 2:
            raise AssertionError("The factor must be greater than or equal to 2.")

        self.upper_bound = upper_bound
        self.factor = factor

    def get_upper_bound(self) -> int:
        """
        Returns the upper bound of the iterator.

        Returns:
            int -- The upper bound of the iterator.
        """
        return self.upper_bound

    def get_factor(self) -> int:
        """
        Returns the factor of the iterator.

        Returns:
            int -- The factor of the iterator.
        """
        return self.factor

    def set_upper_bound(self, updated_upper_bound: int) -> None:
        """
        Sets the upper bound of the iterator.

        Arguments:
            updated_upper_bound {int} -- The updated upper bound of the iterator.
        """
        self.upper_bound = updated_upper_bound 
    
    def __next__(self) -> int:
        """
        Returns the next largest prime number.

        Returns:
            int -- The next largest prime number.

        Time Complexity Analysis:
            Best case: O(1) (if the upper bound is 2)
            Worst case: O(n*log log n) where n is the upper bound
        """
        new_prime = self.generator(self.get_upper_bound())
        new_bound = new_prime * self.get_factor()
        self.set_upper_bound(new_bound)
        return new_prime
    
    def __iter__(self) -> LargestPrimeIterator:
        """
        Returns the iterator.

        Returns:
            LargestPrimeIterator -- The iterator.
        """
        return self

    def generator(self, upper_bound: int) -> int:
        """
        Returns the next largest prime number.

        Arguments:
            upper_bound {int} -- The upper bound of the iterator.

        Returns:
            int -- The next largest prime number.

        Precondition:
            upper_bound >= 2

        Time Complexity Analysis:
            Best case: O(1) (if the upper bound is 2) 
            Worst case: O(n*log log n) where n is the upper bound
        """
        primes = [True for i in range(upper_bound + 1)]
        p = 2

        while p * p <= upper_bound:
            if primes[p]:
                for i in range(p * p, upper_bound + 1, p):
                    primes[i] = False
            p += 1

        for p in range(upper_bound, 1, -1):
            if primes[p]:
                return p