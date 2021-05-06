#https://leetcode.com/problems/single-number-ii/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] = False
            else:
                dictionary[i] = True
        for key, value in dictionary.items():
            if value == True:
                return key