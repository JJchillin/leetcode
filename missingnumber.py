#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxsum = 0
        for i, j in zip(nums, range(1, len(nums) + 1)):
            maxsum = maxsum - i + j
        return maxsum