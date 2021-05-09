#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            if i in myset:
                myset.remove(i)
            else:
                myset.add(i)
        return myset.pop()