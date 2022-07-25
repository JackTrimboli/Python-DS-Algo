'''
Q2: 

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

----------------------------------------------------------------------------

Input: nums = [1], k = 1

Output: [1]
'''
import heapq


# min heapify implementation:

def build_min_heap(arr):
    for i in range(len(arr)//2, 0, -1):
        minHeapify(arr, i)


def minHeapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= len(arr)-1:
        if (arr[i] > arr[l] or arr[i] > arr[r]):
            if arr[l] < arr[r]:
                arr[i], arr[l] = arr[l], arr[i]
                minHeapify(arr, l)
            else:
                arr[i], arr[r] = arr[r], arr[i]
                minHeapify(arr, r)


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2

# IMPLEMENTATION WITH HEAPQ MODULE


def kMostFrequent(nums, k):
    dict = {}

    # map each value in the array to its number of occurances
    for val in nums:
        if val not in dict:
            dict[val] = 1
        else:
            dict[val] += 1

    # get the mapped values in the form of a heap
    heap = []
    for key, val in dict.items():
        heap.append((-val, key))

    heapq.heapify(heap)
    res = []

    # pop k elements from the heap, which gets the k smallest elements
    for item in range(k):
        item, ans = heapq.heappop(heap)
        res.append(ans)
    return res


# IMPLEMENTATION WITH MY OWN HEAP

def kMostFrequent2(nums, k):
    dict = {}

    # map each value in the array to its number of occurances
    for val in nums:
        if val not in dict:
            dict[val] = 1
        else:
            dict[val] += 1

    # get the mapped values in the form of a heap
    heap = []
    for key, val in dict.items():
        heap.append((-val, key))

    build_min_heap(heap)
    res = []

    # pop k elements from the heap, which gets the k smallest elements
    for item in range(k):
        item, ans = heap.pop(0)
        res.append(ans)
        build_min_heap(heap)
    return res


print(kMostFrequent([1, 1, 1, 2, 2, 3], 2))
print(kMostFrequent([1], 1))
print(kMostFrequent2([1, 1, 1, 2, 2, 3], 2))
print(kMostFrequent2([1], 1))
