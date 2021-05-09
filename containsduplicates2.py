https://leetcode.com/problems/contains-duplicate-ii/
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