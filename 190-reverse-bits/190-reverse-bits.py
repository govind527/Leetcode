class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res=(res<<1)# move over to make space new bit
            res=res | (n&1)## add last bit, I used OR instead of XOR and it passed all tests you can use both
            n>>=1#removes last bit from n.
        return res
        