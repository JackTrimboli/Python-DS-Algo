# Recursive implementation of bubble sort:

def bubbleSort_helper(a, end):
    if end != 0:
        flag = False
        for i in range(end - 1):
            if a[i] > a[i+1]:
                flag = True
                a[i], a[i + 1] = a[i + 1], a[i]
        if flag:
            bubbleSort_helper(a, end-1)


def bubbleSort(a):
    bubbleSort_helper(a, len(a))


def bubblesortByMemory(A):
    bubblesortByMemoryHelper(A, 0)


def bubblesortByMemoryHelper(A, i):
    flag = False
    nxt = i + 1
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            flag = True
            A[i], A[i+1] = A[i+1], A[i]
    if flag:
        bubblesortByMemoryHelper(A, nxt)


a = [7, 3, 0, 1, 4]
bubblesortByMemory(a)
print(a)


'''
[7, 3, 0, 1, 4]
[3, 0, 1, 4, 7]
[0, 1, 3, 4, 7]
'''
