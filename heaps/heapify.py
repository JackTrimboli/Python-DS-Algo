
'''
- should do it in place, not through insertion
- assuming the first index is index 1
'''

# turns an array into a max heap


class Heap:
    def __init__(self):
        self.arr = []

    def insert(self, el):
        self.arr.append(el)
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.heapify_up(self.heap_size()-1)

    def heapify_up(self, i):
        # get the parent
        parent = self.get_parent(i)

        # check which is greater
        if self.arr[i] > self.arr[parent]:
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            self.heapify_up(parent)

    def delete(self):
        # swap root with last element
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        # remove from heap
        self.arr.pop()
        # trickle down first element until it finds it's place
        self.heapify_down(0)

    def heapify_down(self, i):

        left = self.get_left_child(i)
        right = self.get_right_child(i)

        # ensure that both children exist
        if left < self.heap_size() - 1 and right < self.heap_size() - 1:
            # check which child is larger
            if self.arr[left] > self.arr[right]:
                if self.arr[left] > self.arr[i]:
                    self.arr[left], self.arr[i] = self.arr[i], self.arr[left]
                    self.heapify_down(left)

            else:
                if self.arr[right] > self.arr[i]:
                    self.arr[right], self.arr[i] = self.arr[i], self.arr[right]
                    self.heapify_down(right)

    def print_heap(self):
        print(self.arr)

    def get_parent(self, i):
        return (i - 1) // 2

    def get_right_child(self, i):
        return i * 2 + 2

    def get_left_child(self, i):
        return i * 2 + 1

    def heap_size(self):
        return len(self.arr)


# def heapsort(A):
#     for i in range(len(A)-1, 1, -1):
#         A[i], A[0] = A[0], A[i]
#         maxHeapify(A, i)


def buildMaxHeap(A):
    for i in range((heapSize(A) // 2 - 1), 0, -1):
        maxHeapify(A, i)


def maxHeapify(A, i):
    l = left(i)
    r = right(i)

    # check if the left or right child is greater than its parent
    if l <= heapSize(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize(A) and A[r] > A[largest]:
        largest = r

    # if the largest is NOT the parent, we need to swap the current parent with largest
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        maxHeapify(A, largest)


def heapSize(A):
    return len(A) - 1


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def parent(i):
    return (i-1)/2


# a = [None, 1, 2, 3, 4, 5, 6, 7]
# buildMaxHeap(a)
# print(a)


myHeap = Heap()
a = []

for e in range(1, 11):
    myHeap.insert(e)
    a.append(e)

buildMaxHeap(a)
heapsort(a)
print(a)
# myHeap.print_heap()
# myHeap.delete()
# myHeap.print_heap()
# myHeap.delete()
# myHeap.print_heap()


'''
OUTPUT

Array Representation
[None, 7, 5, 6, 4, 2, 1, 3]

Tree Representation:

        7
     5     6
    4 2   1 3 

'''
