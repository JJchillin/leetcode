#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        pastnums = {n}
        sumofsquares = 0
        while True:
            while n != 0:
                sumofsquares += (n % 10)**2
                n = n // 10
            n = sumofsquares
            sumofsquares = 0
            if n in pastnums:
                return False
            pastnums.add(n)
            if n == 1:
                return True