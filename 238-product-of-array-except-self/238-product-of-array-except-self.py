# Notes:make two passes, first in-order, second in-reverse, to compute products

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]* len(nums) # in starting we take array of 1's
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix   3# storing in res list 
            prefix=prefix*nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
        return res
        
