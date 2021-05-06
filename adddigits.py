#https://leetcode.com/problems/add-digits/
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