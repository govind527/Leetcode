#Notes :at most two sorted halfs, mid will be apart of left sorted or right sorted, if target is in range of sorted portion then search it, otherwise search other half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=l+(r-l)//2
            
            if target==nums[m]:
                return m
            
            #left sorted array
            if nums[l]<=nums[m]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                
                else:
                    r=m-1
            
            
            else:
                if target<nums[m] or target>nums[r]:
                    r=m-1
                
                else:
                    l=m+1
        return -1
                
        