# Notes:check if half of array is sorted in order to find pivot, arr is guaranteed to be in at most two sorted subarrays

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        left=0
        right=len(nums)-1
        while(left<=right):
            if nums[left]<nums[right]:
                res=min(res,nums[left])
                break
            mid = left+(right-left)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
        return res
