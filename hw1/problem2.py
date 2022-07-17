'''
Problem 2:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6

Output: [1,2]
'''


def findNumbers(nums, target):
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in dict and target - nums[i] != nums[i]:
            return sorted([i,  dict[target - nums[i]]])
    return None


print(findNumbers([2, 7, 11, 15], 9))
print(findNumbers([3, 2, 4], 6))
