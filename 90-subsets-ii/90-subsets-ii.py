class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=set()
        nums.sort()
        for i in range(2**len(nums)):
            sub=[]
            for j in range(len(nums)):
                bit=i&1
                i>>=1
                if bit:
                    sub.append(nums[j])
            subset.add(tuple(sub))
        return subset
                
        