class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lt=[]
        for num in nums:
            if nums.count(num)==1:
                lt.append(num)
        return lt
        