# from ctypes import *
# atoi = cdll.msvcrt.atoi
# atoi(b"415")

# Recursive implementation of selection sort #

def selectionSort_helper(arr, start):
    if start < len(arr) - 1:
        ndx = start
        for i in range(start + 1, len(a)):
            if arr[i] < arr[ndx]:
                ndx = i
        arr[ndx], arr[start] = arr[start], arr[ndx]
        selectionSort_helper(arr, start + 1)


def selectionSort(a):
    selectionSort_helper(a, 0)


a = [7, 3, 0, 1, 4]
selectionSort(a)
print(a)
# OUTPUT: [0, 1, 3, 4, 7]
