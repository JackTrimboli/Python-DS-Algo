'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.­
'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalancedBT(root):
    # If the tree is empty, it's balanced
    if root == None:
        return True

    # Check the height of the left subtree
    ltree = depth(root.left)

    # Check the height of the left subtree
    rtree = depth(root.right)

    # Return the comparison
    return (abs(ltree-rtree) < 2) and isBalancedBT(root.left) and isBalancedBT(root.right)


def depth(curr):
    if curr == None:
        return 0

    leftDepth = depth(curr.left)
    rightDepth = depth(curr.right)

    if leftDepth > rightDepth:
        return leftDepth + 1
    return rightDepth + 1


# manually make testcases
test1 = Node(3)
test1.right = Node(20)
test1.right.right = Node(7)
test1.right.left = Node(15)
test1.left = Node(9)

test2 = Node(1)
test2.right = Node(2)
test2.left = Node(2)
test2.left.left = Node(3)
test2.left.left = Node(4)
test2.left.right = Node(3)
test2.left.left.right = Node(4)

print(isBalancedBT(test1))
print(isBalancedBT(test2))
