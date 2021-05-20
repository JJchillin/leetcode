#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

#Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = False
        length = len(nums) - 1
        i = 2
        while i <= length:
            if nums[i - 2] == nums[i - 1] and nums[i - 2] == nums[i]:
                nums.pop(i)
                length = length - 1
                i = i - 1
            i = i + 1
        return len(nums)
