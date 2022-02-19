#Notes :modulo, and dividing n; mod and div are expensive, to divide use bit shift, instead of mod to get 1's place use bitwise & 1;

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            n=n & (n-1)
            res+=1
        return res
        