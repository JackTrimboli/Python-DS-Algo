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


a = [7, 3, 0, 1, 4]
bubbleSort(a)
print(a)
