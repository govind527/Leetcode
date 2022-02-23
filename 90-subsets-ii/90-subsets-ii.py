# this solution is same as solution of subset-i
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=set()
        nums.sort()	    # Sort to assist check for adjacent elements to avoid duplicates

        for i in range(2**len(nums)):
            sub=[]
            for j in range(len(nums)):
                bit=i&1
                i>>=1
                if bit:
                    sub.append(nums[j])
            subset.add(tuple(sub))
        return subset
                
        
