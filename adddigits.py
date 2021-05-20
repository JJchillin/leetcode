#https://leetcode.com/problems/add-digits/
#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        sumdigits = 0
        while num >= 10:
            while num != 0:
                sumdigits = sumdigits + num % 10
                num = num // 10
            num = sumdigits
            sumdigits = 0
        return num
