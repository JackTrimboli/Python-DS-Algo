def moveZeroes(nums: list[int]) -> None:
    idx = len(nums) - 1

    for i in range(len(nums)):
        if nums[i] == 0:
            while nums[idx] == 0:
                idx = - 1
            if idx <= i:
                break
            nums[i] = nums[idx]
            nums[idx] = 0
            idx -= 1
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
