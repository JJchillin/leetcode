#https://leetcode.com/problems/merge-sorted-array/
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