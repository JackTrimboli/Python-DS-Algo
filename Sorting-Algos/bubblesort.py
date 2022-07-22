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


def bubbleSortByMemory_helper(A, end):
    if end != 0:
        flag = False
        for i in range(0, end - 1):
            if A[i] > A[i + 1]:
                flag = True
                A[i], A[i + 1] = A[i], A[i + 1]  # "bubble up" larger elements
        if flag:
            bubbleSort_helper(A, end - 1)


def bubbleSortByMemory(A):
    bubbleSortByMemory_helper(A, len(A))


a = [7, 3, 0, 1, 4]
bubbleSortByMemory(a)
print(a)


'''
[7, 3, 0, 1, 4]
[3, 0, 1, 4, 7]
[0, 1, 3, 4, 7]
'''
