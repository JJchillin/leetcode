https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        myset = set()
        for i in range(1, len(nums) + 1):
            myset.add(i)
        for num in nums:
            if num in myset:
                myset.remove(num)
        return myset