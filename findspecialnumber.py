#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
#Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 4:
            return arr[0]
        mydict = {}
        for i in arr:
            if i in mydict:
                mydict[i] += 1
                if mydict[i] > len(arr) // 4:
                    return i
            else:
                mydict[i] = 1
