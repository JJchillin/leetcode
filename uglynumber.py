#https://leetcode.com/problems/ugly-number/
#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#Given an integer n, return true if n is an ugly number.
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False 
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True
