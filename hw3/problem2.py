# use hashmaps for linear time algo

'''
Problem 2:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6],

target = 5

Output: 2

 

Example 2:

Input: nums = [1,3,5,6],

target = 2

Output: 1
'''

# linear solution


def findTarget(nums, target):
    prev = 0
    for i in range(len(nums)):
        if nums[i] > target:
            return prev + 1
        if nums[i] != target:
            prev = i
        else:
            return i


print(findTarget([1, 3, 5, 6], 2))

print(findTarget([1, 3, 5, 6], 5))
