'''
Q2: 


Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
'''

res = []


def getUniqueCombos(candidates, target):
    getCombos(0, [], 0, candidates, target)
    return res


def getCombos(i, curr, currSum, candidates, target):
    # base case (bad combo): idx out of bounds or the current sum is greater than target
    if i >= len(candidates) or currSum > target:
        return

    # base case (good combo): we've hit our target, add combination to result and return
    if currSum == target:
        res.append(curr.copy())
        return

    # if the base cases aren't hit, make two dfs calls: one where we add candidates[i] to our sum and one where we do not
    curr.append(candidates[i])
    getCombos(i, curr, currSum+candidates[i], candidates, target)

    curr.pop()
    getCombos(i+1, curr, currSum, candidates, target)


print(getUniqueCombos([2, 3, 6, 7], 7))
res = []
print(getUniqueCombos([2, 3, 5], 8))
res = []
print(getUniqueCombos([2], 1))
