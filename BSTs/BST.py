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
        z.p = y

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

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


t = BST()
for e in [11, 16, 15, 12, 4, 20, 60]:
    t.insert(e)

print("contains 12?: ", t.contain(12))

print("contains 5?: ", t.contain(5))

print("contains 12?: ", t.contain_iterative(12))

print("contains 5?: ", t.contain_iterative(5))
