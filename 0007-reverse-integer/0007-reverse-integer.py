class Solution:
    def reverse(self, x):
        MIN_INT = -2147483648
        MAX_INT = 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        result *= sign

        if result < MIN_INT or result > MAX_INT:
            return 0

        return result
