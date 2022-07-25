import random


class Node:
    def __init__(self, key):
        self.key = key
        self.next = [None] * 32
        self.height = -1


class Skiplist:
    def __init__(self):
        self.tower = Node(None)

    def clear(self):
        self.tower = Node(None)

    def is_empty(self):
        return self.tower.height == -1

    def contains(self, key):
        curr = self.tower.next[height]
        level = self.height

        while level >= 0:
            # move to the right until we hit a value that is greater than the key we are looking for
            while curr.next[level] is not None and curr.next[level].key < key:
                curr = curr.next[level]
            level -= 1
        return curr.next[0] is not None and curr.next[0].key == key

    def put(self, key):
        curr = self.tower.next[height]
        level = self.height

        while level >= 0:
            # move to the right until we hit a value that is greater than the key we are looking for
            while curr.next[level] is not None and curr.next[level].key < key:
                curr = curr.next[level]
            level -= 1
        '''
        TODO:
        1. fix next ptrs
        2. keep track of when we move down (node)
        3. determine height of inserted node
        '''

    def remove(self, key):
        return

    def keys(self):
        res = []
        node = self.tower
        while node != None:
            res.append(node.key)
            node = node.next[0]
        return res

    def get_random_count(self):
        count = 0
        for i in range(32):
            if random.randint(0, 1) == 1:
                count += 1
            else:
                break
        return count
