'''
Problem 2:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''


def findMedianSortedArrays(nums1, nums2):

    # Find the larger array
    if len(nums1) > len(nums2):
        larger = nums2
        smaller = nums1
    else:
        larger = nums1
        smaller = nums2

    # store m and n
    m = len(larger)
    n = len(smaller)

    left_part = (m + n + 1) // 2
    left = 0
    right = m
    even = ((m + n) % 2) == 0

    # binary search tp find our median
    while left <= right:

        # get midpoint of each array
        large_mid = (left + right) // 2
        small_mid = left_part - large_mid

        # split the array into 2 partitions and determine the leftmost/rightmost values
        if large_mid == 0:
            large_leftmax = float("-inf")
        else:
            large_leftmax = larger[large_mid - 1]

        if large_mid == m:
            large_rightmin = float("inf")
        else:
            large_rightmin = larger[large_mid]

        if small_mid == 0:
            small_leftmax = float("-inf")
        else:
            small_leftmax = smaller[small_mid - 1]

        if small_mid == n:
            small_rightmin = float("inf")
        else:
            small_rightmin = smaller[small_mid]

        # compare the bounds of each partition to see if we've found the median

        # if bounds overlap and we have an even num elements, return the avg to get the median
        if large_leftmax <= small_rightmin and small_leftmax <= large_rightmin and even:
            leftmax = max(large_leftmax, small_leftmax)
            rightmin = min(large_rightmin, small_rightmin)
            return float((leftmax + rightmin) / 2)

        # if bounds overlap and we have an odd num elements, return the median
        elif large_leftmax <= small_rightmin and small_leftmax <= large_rightmin:
            leftmax = max(large_leftmax, small_leftmax)
            return float(leftmax)

        # if we reach this line we haven't found the median and must continue binary search until conditions are met
        elif large_leftmax > small_rightmin:
            right = large_mid - 1

        elif small_leftmax > large_rightmin:
            left = large_mid + 1


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
print(findMedianSortedArrays([0, 0], [0, 0]))
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([2], []))
