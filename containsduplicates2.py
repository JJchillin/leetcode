#https://leetcode.com/problems/contains-duplicate-ii/
#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                if abs(i - mydict[nums[i]]) <= k:
                    return True
                else:
                    mydict[nums[i]] = i
            else:
                mydict[nums[i]] = i
        return False
