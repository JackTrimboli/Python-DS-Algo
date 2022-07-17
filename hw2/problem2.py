'''
Problem 2:

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Input: nums = [3,0,1]

Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

 

Bonus Point : Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

'''


def missingNumber(nums: list[int]) -> int:
    dict = {}
    for i in nums:
        dict[i] = i
    for i in range(len(nums)):
        if i not in dict:
            return i
    return i + 1


def missingNumber2(nums: list[int]) -> int:
    expected = len(nums)*int((len(nums)+1)/2)
    actual = sum(nums)
    return expected - actual


print(missingNumber([3, 0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

print(missingNumber2([3, 0, 1]))
print(missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
