# from ctypes import *
# atoi = cdll.msvcrt.atoi
# atoi(b"415")

# Recursive implementation of selection sort #

def selectionSort_helper(arr, start):
    # If the starting index is less than the last index, do the work.
    if start < len(arr) - 1:
        ndx = start
        # for each value from the second idx to the last idx
        for i in range(start + 1, len(a)):
            # check if the value is less than arr at start
            if arr[i] < arr[ndx]:
                # if it is, swap
                ndx = i
        # swap start with smallest value in the array
        arr[ndx], arr[start] = arr[start], arr[ndx]
        selectionSort_helper(arr, start + 1)


def selectionSort(a):
    selectionSort_helper(a, 0)


def selectionSortByMemory_helper(A, i):
    ndx = i
    for j in range(i+1, len(A)):
        if A[j] < A[ndx]:
            ndx = j

    A[ndx], A[i] = A[i], A[ndx]
    selectionSort_helper(A, i + 1)


def selectionSortByMemory(A):
    selectionSortByMemory_helper(A, 0)


a = [7, 3, 0, 1, 4]
b = [7, 3, 0, 1, 4]
selectionSort(a)
print(a)
selectionSortByMemory(b)
print(b)
# OUTPUT: [0, 1, 3, 4, 7]
