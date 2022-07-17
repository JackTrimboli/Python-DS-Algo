'''
Problem 1:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]

 

Input: nums = [0]

Output: [0]
'''


def moveZeroes(nums: list[int]) -> list[int]:
    idx = 0
    temp = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = 0
            nums[idx] = temp
            idx += 1


testcase1 = [0, 1, 0, 3, 12]
testcase2 = [0]
moveZeroes(testcase1)
moveZeroes(testcase2)
print(testcase1)
print(testcase2)
