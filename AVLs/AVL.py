class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.key = None


class AVL:

    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, x):
        if x is None:
            return -1
        lh = self.height_helper(x.left)
        rh = self.height_helper(x.right)

        return 1 + max(lh, rh)
