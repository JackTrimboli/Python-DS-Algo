class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.key = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        z = Node()
        z.key = key
        x = self.root
        y = None

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, key):
        # first find the key we want to delete
        curr = self.root
        while curr != None and curr.key != key:
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        # now that we have found the node, we have to determine it's status
        if curr == None:
            return False
        # is leaf:
        if curr.left is None and curr.right is None:
            if curr.parent.right == curr:
                curr.parent.right = None
            else:
                curr.parent.left = None
            return True
        # has just left child:
        if curr.left != None and curr.right == None:
            curr.left.parent = curr.parent
            curr = curr.left
            return True
        # has just right child:
        elif curr.right != None and curr.left == None:
            curr.right.parent = curr.parent
            curr = curr.right
            return True
        # Has two children
        else:
            # replacement should contain the smallest value of the right subtree
            replacement = self.minimum_as_node(curr.right)
            # swap the keys
            curr.key = replacement.key
            if replacement.right != None:
                replacement = replacement.right
            else:
                replacement.parent = None
            return True

    def inorder(self):
        # nodes should print sorted
        self.inorder_helper(self.root)

    def inorder_helper(self, root):
        if root is None:
            return
        self.inorder_helper(root.left)
        print(root.key)
        self.inorder_helper(root.right)

    def preorder(self):
        # print root first then children
        self.preorder_helper(self.root)

    def preorder_helper(self, root):
        if root is None:
            return
        print(root.key)
        self.preorder_helper(root.left)
        self.preorder_helper(root.right)

    def minimum(self):
        n = self.root
        while n.left is not None:
            n = n.left
        return n.key

    def minimum_as_node(self):
        n = self.root
        while n.left is not None:
            n = n.left
        return n

    def maximum(self):
        n = self.root
        while n.right is not None:
            n = n.right
        return n.key

    def contain_helper(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif root.key < key:
            return self.contain_helper(root.right, key)
        else:
            return self.contain_helper(root.left, key)

    def contain(self, key):
        return self.contain_helper(self.root, key)

    def contain_iterative(self, k):
        x = self.root
        while x is not None and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return x is not None

    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, x):
        if x is None:
            return -1
        lh = self.height_helper(x.left)
        rh = self.height_helper(x.right)
        return 1 + max(lh, rh)


t = BST()
for e in [11, 16, 15, 12, 4, 20, 60]:
    t.insert(e)

print(t.height())
