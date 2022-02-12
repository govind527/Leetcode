#Notes:hashset to get unique values in array, to check for duplicates easily

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)   
        return False
        