#https://leetcode.com/problems/find-peak-element/
#A peak element is an element that is strictly greater than its neighbors.

#Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        if nums[0] > nums[1]:
             return 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return -1
