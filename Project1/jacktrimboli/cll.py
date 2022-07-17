from operator import is_


class Node:
    def __init__(self, elm, prv, nxt):
        self.elm = elm
        self.prv = prv
        self.nxt = nxt


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push_front(self, elm):
        if self.head is None:
            # create new node
            node = Node(elm, None, None)
            # head and tail and the same
            self.head = node
            self.tail = node
        else:
            # create new node
            node = Node(elm, None, self.head)
            # head becomes second in the list
            self.head.prv = node
            # head becomes the new node
            self.head = node
            # tail points to the new head
            self.tail.nxt = self.head
            # heads prev becomes tail
            self.head.prv = self.tail

    def pop_front(self):
        node = self.head
        # if list is of size one or less
        if node.nxt is None:
            self.head = None
            self.tail = None
        # otherwise
        else:
            self.head = node.nxt
            # the new head's prev points to tail
            self.head.prv = self.tail
            # tail points to the new head
            self.tail.nxt = self.head
        return node.elm

    def push_back(self, elm):
        if self.head is None:
            node = Node(elm, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(elm, self.tail, None)
            self.tail.nxt = node
            self.tail = node
            # the new tail points to head next
            self.tail.nxt = self.head
            # the head's prev points to the new tail
            self.head.prv = self.tail

    def pop_back(self):
        node = self.tail
        if node.prv is None:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prv
            self.tail.nxt = self.head
            self.head.prv = self.tail
        return node.elm

    def eliminate(self, node):
        if self.is_empty():
            return
        if node == self.head:
            self.pop_front()
        elif node == self.tail:
            self.pop_back()
        else:
            curr = self.head
            while curr != node:
                curr = curr.nxt
            curr.prv.nxt = curr.nxt
            curr.nxt.prv = curr.prv
