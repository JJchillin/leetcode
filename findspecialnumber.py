https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
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