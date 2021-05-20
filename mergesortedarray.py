#https://leetcode.com/problems/merge-sorted-array/
#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                itr = m + j
                while itr != i - 1:
                    nums1[itr] = nums1[itr - 1]
                    itr = itr - 1
                nums1[i] = nums2[j]
                j = j + 1
            elif m + n - i == n - j:
                nums1[i] = nums2[j]
                j = j + 1
            i = i + 1
        return nums1
