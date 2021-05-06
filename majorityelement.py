#https://leetcode.com/problems/majority-element/solution/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] = mydict[i] + 1
            else:
                mydict[i] = 1
            if mydict[i] > len(nums)/2:
                return i