""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev, with edits by Jackson Goerner'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic, List
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ 
    Self-balancing binary search tree using rebalancing by sub-tree rotations of Adelson-Velsky and Landis (AVL).

    Attributes:
        root {AVLTreeNode} -- The root node of the tree
        length {int} -- The length of the tree

    Unless specified, all functions have time complexity of O(1).
    """

    def __init__(self) -> None:
        """
        Initialises an empty Binary Search Tree
        """
        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
        Get the height of a node. Return current.height if current is not None. Otherwise, return 0.
        
        Arguments:
            current {AVLTreeNode} -- The current node to get the height of

        Returns:
            int -- The height of the node

        Precondition:
            The node must be in the tree
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it.

        Arguments::
            current {AVLTreeNode} -- The current node to check for insertion
            key {K} -- The key to check for insertion
            item {I} -- The item to insert

        Time Complexity Analysis:
            Best Case: O(log(n)) - if the tree is balanced
            Worst Case: O(log(n)) - if the tree is unbalanced
        """
        if current is None:
            current = AVLTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        return self.rebalance(current)

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
        Attempts to delete an item from the tree, it uses the Key to determine the node to delete.

        Arguments:
            current {AVLTreeNode} -- The current node to check for deletion
            key {K} -- The key to check for deletion

        Returns:
            AVLTreeNode -- The new node to replace the current node

        Precondition:
            The key must be in the tree

        Time Complexity Analysis:
            Best Case: O(log(n))
            Worst Case: O(log(n))
        """
        if current is None:
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            succ = self.get_successor(current)
            if succ is not None:
                current.key  = succ.key
                current.item = succ.item
                current.right = self.delete_aux(current.right, succ.key)
        
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

        return self.rebalance(current)

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)

        Arguments:
            current {AVLTreeNode} -- The current node to rotate

        Returns:
            AVLTreeNode -- The new rotated node
        """
        child = current.right
        current.right = child.left
        child.left = current
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))
        return child


    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)

        Arguments:
            current {AVLTreeNode} -- The current node to rotate

        Returns:
            AVLTreeNode -- The new rotated node
        """
        child = current.left
        current.left = child.right
        child.right = current
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))
        return child

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.

        Arguments:
            current {AVLTreeNode} -- The current node to check for rebalancing

        Returns:
            AVLTreeNode -- The new root of the subtree
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def range_between(self, i: int, j: int) -> List:
        """
        Returns a list of smallest entries in the tree from i th to j th inclusive, using recursion
        i and j can take the values between 0 to (n - 1) where n is the number of nodes in the tree.
        the 0th entry stores the smallest value in the tree.

        Returns:
            List -- A list of the smallest entries in the tree from i th to j th inclusive

        Time Complexity Analysis:
            Best Case: O(log(n))
            Worst Case: O(log(n))
        """
        if i > j:
            return []
        if i < 0 or j > self.length - 1:
            raise ValueError('Invalid range')
        return self.range_between_aux(self.root, i, j)

    def range_between_aux(self, current: AVLTreeNode, i: int, j: int) -> List:
        """
        Returns a list of smallest entries in the tree from i th to j th inclusive, using recursion
        i and j can take the values between 0 to (n - 1) where n is the number of nodes in the tree.
        the 0th entry stores the smallest value in the tree.

        Returns:
            List -- A list of the smallest entries in the tree from i th to j th inclusive

        Time Complexity Analysis:
            Best Case: O(log(n))
            Worst Case: O(log(n))
        """
        if current is None:
            return []
        if i == 0 and j == self.length - 1:
            return self.inorder(current)
        if i == 0:
            return self.inorder(current)[:j + 1]
        if j == self.length - 1:
            return self.inorder(current)[i:]
        return self.inorder(current)[i:j + 1]

    def inorder(self, current: AVLTreeNode) -> List:
        """
        Returns a list of smallest entries in the tree, using recursion

        Arguments:
            current {AVLTreeNode} -- The current node to check for rebalancing

        Returns:
            List -- The list of smallest entries in the tree

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        if current is None:
            return []
        return self.inorder(current.left) + [current.item] + self.inorder(current.right)