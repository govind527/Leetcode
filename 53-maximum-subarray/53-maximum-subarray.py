#Notes: pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0
        for i in nums:
            if curSum<0:
                curSum=0
            curSum+=i
            maxSub=max(maxSub,curSum)
        return maxSub
        