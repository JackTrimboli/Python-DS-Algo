class Node:
    def __init__(self):
        self.key = self.value = self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def contains(self, key):
        x = self.root
        while x is not None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

        return x is not None

    def put(self, key, value):
        z = Node()
        z.key = key
        z.value = value
        x = self.root
        y = None

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def get(self, key):
        """Returns the value paired with the specified key"""
        curr = self.root
        while curr != None and curr.key != key:
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        if curr:
            return curr.value
        return None

    def remove(self, key):
        # first find the key we want to delete
        curr = parent = self.root

        while curr != None and curr.key != key:
            parent = curr
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        # now that we have found the node, we have to determine it's status
        if curr == None:
            return False

        # is leaf:
        if curr.left is None and curr.right is None:
            if parent.right == curr:
                parent.right = None
            else:
                parent.left = None
            return True

        # has just left child:
        if curr.left != None and curr.right == None:
            if parent.right == curr:
                parent.right = curr.left
            else:
                parent.left = curr.left
            return True

        # has just right child:
        elif curr.right != None and curr.left == None:
            if parent.right == curr:
                parent.right = curr.right
            else:
                parent.left = curr.right
            return True

        # Has two children
        else:
            # replacement should contain the smallest value of the right subtree
            replacement = self.minimum_as_node(curr.right)
            # swap the keys
            curr.key = replacement.key
            curr.value = replacement.value
            if replacement.right != None:
                replacement = replacement.right
            else:
                replacement = None
            return True

    def inorder(self):
        # nodes should print sorted
        self.inorder_helper(self.root)

    def inorder_helper(self, root):
        if root is None:
            return
        self.inorder_helper(root.left)
        print(root.key + ", " + root.value)
        self.inorder_helper(root.right)

    def keys_helper(self, root, arr):
        if root is None:
            return None
        self.keys_helper(root.left, arr)
        arr.append(root.key)
        self.keys_helper(root.right, arr)

    def keys(self):
        arr = []
        self.keys_helper(self.root, arr)
        return arr

    def minimum(self):
        n = self.root
        while n.left is not None:
            n = n.left
        return n.key

    def minimum_as_node(self, node):
        n = node
        while n.left is not None:
            n = n.left
        return n

    def maximum(self):
        n = self.root
        while n.right is not None:
            n = n.right
        return n.key
