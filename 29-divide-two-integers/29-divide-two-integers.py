class Solution:
    def divide(self, A: int, B: int) -> int:
        # Easy but slow
        
        # if not dividend:
        # return 0
        # sign = 1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 0
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        # res = 0
        # while dividend >= divisor:
        # dividend -= divisor
        # res += 1
        # return -res if sign else res
        
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res
        