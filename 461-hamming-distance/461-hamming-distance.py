#Notes:We need to count number of positions at which the bits differ for given numbers x and y. 
#For this, we can use bit-wise XOR. The xor of two bits is set only if they differ. So, we need to xor and count the number of set bits in it.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor=x^y
        ans=0
        while xor:
            ans+=xor&1
            xor>>=1
        return ans
        
