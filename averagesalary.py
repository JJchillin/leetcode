#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
#Given an array of unique integers salary where salary[i] is the salary of the employee i.
#Return the average salary of employees excluding the minimum and maximum salary.
class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = salary[0]
        maximum = 0
        total = 0
        for i in salary:
            if minimum > i:
                minimum = i
            if maximum < i:
                maximum = i
            total = total + i
        total = total - minimum - maximum
        return float(total / (len(salary) - 2))
