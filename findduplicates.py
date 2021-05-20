#https://leetcode.com/problems/find-all-duplicates-in-an-array/

#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        myset = set()
        duplicateset = set()
        for i in nums:
            if i in myset:
                duplicateset.add(i)
            else:
                myset.add(i)
        return duplicateset
