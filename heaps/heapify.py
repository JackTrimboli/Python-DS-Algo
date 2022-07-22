
'''
- should do it in place, not through insertion
- assuming the first index is index 1
'''
from heapq import heapify


def buildMaxHeap(A):
    for i in range((heapSize(A) // 2), 0, -1):
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
    return 2*i


def right(i):
    return 2*i+1


def parent(i):
    return i/2


a = [None, 1, 2, 3, 4, 5, 6, 7]
buildMaxHeap(a)
print(a)


'''
OUTPUT

Array Representation
[None, 7, 5, 6, 4, 2, 1, 3]

Tree Representation:

        7
     5     6
    4 2   1 3 

'''
