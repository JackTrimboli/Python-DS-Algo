
'''
*** Implementation of merge sort ***
- Cut the array in half.
- Sort the left half.
- sort the right half.
- Merge the two sorted halves into one sorted array


[7, 12, 3, 4, 6, 1]
[7, 12, 3], [4,6,1]

[7] [12, 3],   [4] [6,1]
[7] [12] [3] [4] [6] [1]
'''


def mergeSort(a):
    # base case for splitting
    if len(a) < 2:
        return

    # recursive case for splitting
    midpoint = len(a) // 2
    leftSub = a[:midpoint]
    rightSub = a[midpoint:]
    mergeSort(leftSub)
    mergeSort(rightSub)

    # begin merge
    i = 0
    while len(leftSub) != 0 and len(rightSub) != 0:
        if leftSub[0] < rightSub[0]:
            a[i] = leftSub.pop(0)
        else:
            a[i] = rightSub.pop(0)
        i += 1

    # one list is empty now, empty the other list. One loop will run the other will not
    while len(leftSub) != 0:
        a[i] = leftSub.pop(0)
        i += 1

    while len(rightSub) != 0:
        a[i] = rightSub.pop(0)
        i += 1


a = [7, 12, 3, 4, 6, 1]
mergeSort(a)
print(a)
