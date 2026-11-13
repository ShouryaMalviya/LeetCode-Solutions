import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Numbers less than or equal to 1 cannot be perfect numbers
        if num <= 1:
            return False
        
        # Start with 1, as 1 is a proper divisor for any num > 1
        sum_div = 1
        
        # Iterate up to the square root of num
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                sum_div += i
                # Add the paired divisor if it's distinct from i
                if i * i != num:
                    sum_div += num // i
                    
        return sum_div == num