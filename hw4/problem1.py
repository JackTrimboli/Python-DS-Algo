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


def connectSticks(self, sticks: list[int]) -> int:  # heapify the stick array
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


'''
Greedy algo
combine two smallest
merge
repeat
'''