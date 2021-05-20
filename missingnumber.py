#https://leetcode.com/problems/missing-number/
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxsum = 0
        for i, j in zip(nums, range(1, len(nums) + 1)):
            maxsum = maxsum - i + j
        return maxsum
