#https://leetcode.com/problems/single-number-ii/
#Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

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
