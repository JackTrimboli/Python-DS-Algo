
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
