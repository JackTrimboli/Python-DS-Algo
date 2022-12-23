

from re import M


class HashMap:
    def __init__(self, tableSize):
        self.T = [None] * tableSize

    def insert(self, key):

        for i in range(len(self.T)-1):
            q = hash(key, i)
            if self.T[q] == None:
                self.T[q] = key
                return q
        print('overflow error')

    def search(self, key):
        i = 0
        while i != len(self.T) or self.T[q] != None:
            q = hash(key, i)
            if self.T[q] == key:
                return q
            i += 1
        return None


# TESTS:

myMap = HashMap(100)

myMap.insert("test")
myMap.insert(55)
myMap.insert("woot")
