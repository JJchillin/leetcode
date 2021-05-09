https://leetcode.com/problems/find-all-duplicates-in-an-array/
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