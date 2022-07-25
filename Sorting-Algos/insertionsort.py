
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insertion A[j] into the sorted sequence from 1 - j-1

        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


a = [5, 1, 8, 11, 6]
insertionSort(a)
print(a)
