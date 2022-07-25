'''
Q1: 

You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Input: sticks = [2,4,3]

Output: 14

Explanation: You start with sticks = [2,4,3].

Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

-----------------------------------------------------------------------------

Input: sticks = [1,8,3,5]

Output: 30

Explanation: You start with sticks = [1,8,3,5].

Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

-------------------------------------------------------------------------------

Input: sticks = [5]

Output: 0

Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.
'''
import heapq

# min heapify implementation:


def build_min_heap(arr):
    for i in range(len(arr)//2, 0, -1):
        minHeapify(arr, i)


def minHeapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= len(arr)-1 and r <= len(arr)-1:
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


def connectSticks(sticks: list[int]) -> int:  # heapify the stick array

    heapq.heapify(sticks)

    cost = 0
    minCost = 0
    while len(sticks) > 1:
        cost += heapq.heappop(sticks)
        cost += heapq.heappop(sticks)
        minCost += cost
        heapq.heappush(sticks, cost)
        cost = 0

    return minCost


# IMPLEMENTATION WITH MY OWN HEAP:

def connectSticks2(sticks: list[int]) -> int:  # heapify the stick array

    build_min_heap(sticks)

    cost = 0
    minCost = 0
    while len(sticks) > 1:
        cost += sticks.pop(0)
        build_min_heap(sticks)

        cost += sticks.pop(0)
        minCost += cost

        sticks.append(cost)
        build_min_heap(sticks)
        cost = 0

    return minCost


print(connectSticks([2, 4, 3]))
print(connectSticks([1, 8, 3, 5]))

print(connectSticks2([2, 3, 4]))
print(connectSticks2([1, 3, 5, 8]))
