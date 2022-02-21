#Notes:compute expected sum - real sum; xor n with each index and value;

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)+1):                   #XOR result with complete number sequence
            res ^=i
        for i in nums:                                 #XOR result with values in nums
            res^=i
        return res
    
#Input: nums = [3,0,1]
    
# result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3) ^ ( 3 ^ 0 ^ 1)

# XOR of same values cancel each other out 

# result = (0) ^ (0 ^ 0)  ^ (1^1) ^ (2) ^ (3^3)
# result =  0 ^ 0 ^ 0 ^ 2 ^ 0
# result = 2
        