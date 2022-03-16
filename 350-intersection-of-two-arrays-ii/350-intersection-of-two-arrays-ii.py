class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
#         Solution 1. We could use one hash map to store all the counts of each element in the shorter array, then loop through the second array to find all possible intersection and return;
# Quick tip: you want to always build your hash map on top of the shorter array, so that the space complexity could be minimized.

# Solution 2. We can sort both arrays first, then use two pointers to loop through both sorted arrays, whenever we encounter two elements from each array that equal, we'll add it to the final result.
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans    
        