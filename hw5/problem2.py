'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

'''


from turtle import left


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertToBST(arr):
    # if array is empty, return empty tree
    if not arr:
        return None

    # find middle of sorted arr
    midpoint = len(arr) // 2

    # root of tree / subtree is equal to the midpoint (in a sorted array, the midpoint must be the root for the tree to be balanced)
    root = Node(arr[midpoint])
    # repeat operation for left/right subtrees
    leftTree = arr[:midpoint]
    rightTree = arr[midpoint+1:]
    root.left = convertToBST(leftTree)
    root.right = convertToBST(rightTree)

    # return tree
    return root


convertToBST([-10, -3, 0, 5, 9])
convertToBST([1, 3])
