"""A set of length n has 2^n subsets. The idea is to iterate over the interval [0, 2^len(nums)-1] and construct a unique subset of nums in each iteration. To achive this, we take an n-bit binary representation of the number we're at in an iteration and interpret it to be a mask of the array. So, we'll decide whether to include or exclude the element at position i (nums[i]) based on whether the bit at position i is 1 or 0 respectively.

For e.g., if nums is [1,2,3], then
0th iteration -> 000 -> []
3rd iteration -> 011 -> [2,3]
7th iteration -> 111 -> [1,2,3]

Note: To get the bits for the ith iteration, we can do the following N number of times (where N == len(nums)):

Get the last bit of i by ANDing it with 1. Examples:
a. i = 3 -> 011 & 001 = 001 = 1
b.i = 4 -> 100 & 001 = 000 = 0
Right shift i by 1 place so that next time step#1 gives the next least significant bit of i."""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        for i in range(2**len(nums)):
            sub=[]
            for j in range(len(nums)):
                lastbit=i&1
                i>>=1
                if lastbit:
                    sub.append(nums[j])
            subset.append(sub)
        return subset
        