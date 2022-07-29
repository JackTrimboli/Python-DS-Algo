'''
Q1: 


Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

You must write an algorithm with O(n) runtime complexity.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

 

Example 2:

Input: nums = [1]

Output: 1

 

Example 3:

Input: nums = [5,4,-1,7,8]

Output: 23
'''


def getMaxSubArray(arr):
    # from 1 to n
    for i in range(1, len(arr)):
        # if prev idx is a positive value
        if arr[i-1] > 0:
            # add the prev idx to curr idx
            arr[i] += arr[i-1]
    # return the sum of the max subarray
    return max(arr)

# Testcases:


print(getMaxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(getMaxSubArray([1]))
print(getMaxSubArray([5, 4, -1, 7, 8]))
