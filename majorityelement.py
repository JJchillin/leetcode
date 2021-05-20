#https://leetcode.com/problems/majority-element/solution/
#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

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
