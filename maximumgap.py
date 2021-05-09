#https://leetcode.com/problems/maximum-gap/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxgap = 0
        for i in range(len(nums) - 1):
            if abs(nums[i+1] - nums[i]) > maxgap:
                maxgap = abs(nums[i+1] - nums[i])
        return maxgap