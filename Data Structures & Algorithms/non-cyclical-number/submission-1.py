class Solution:
    def isHappy(self, n: int) -> bool:
        #ok so add up the sums the first time and then keep looping until a variable like sum is = 1. Somehow track the previous sums. If sum = 1 return true. If you see a sum equal to a previously seen value return False.

        seen = set()

        while n != 1:
            sumN = 0
            for c in str(n):
                sumN += int(c) ** 2

            if sumN in seen:
                return False
            
            if sumN == 1:
                break
        
            seen.add(sumN)

            n = sumN
        
        return True