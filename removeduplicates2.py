https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
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