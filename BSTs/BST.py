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


t = BST()

for e in [11, 16, 15, 12, 4, 20, 60]:
    t.insert(e)

t.inorder()
