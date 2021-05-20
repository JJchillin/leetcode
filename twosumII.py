#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

#Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        i = 0
        while i < len(numbers) - 1:
            j = i + 1
            while j < len(numbers):
                while numbers[i] == numbers[j] and numbers[i] + numbers[j] != target:
                    i = i + 2
                    j = j + 2
                if numbers[i] + numbers[j] == target:
                    answer.append(i + 1)
                    answer.append(j + 1)
                    return answer
                # print(numbers[i], numbers[j])
                j = j + 1
            i = i + 1
        return answer
