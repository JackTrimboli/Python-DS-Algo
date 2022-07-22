'''
uses divide and conquer method 

- sorts a subarray A[p:r]
- Divide by paritioning (rearranging the array A[p:r] into two (possibly empty) subarrays)
- 
'''


def partition(A, p, r):
    x = A[r]                                # Our pivot value
    i = p - 1                               # highest index into the low side
    for j in range(p, r):                   # process each element other than the pivot
        if A[j] <= x:                       # does this element belong on the low side?
            i = i + 1                       # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]         # put this element there
    # pivot goes just to the right of the low side
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1                            # new index of the pivot


def quickSort(A, p, r):
    # parition (rearrange) the subarray around the pivot, which ends up in A[q]
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)                # recursively sort the low side
        quickSort(A, q+1, r)                # recursively sort the high side


arr = [None, 6, 5, 4, 3, 2, 1]
quickSort(arr, 1, len(arr)-1)
print(arr)
