class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ##1. a simple linear scan to three quarters length will work;
        ## 2. or, a binary search could do the job as well.
        quater=len(arr)//4
        for i in range(len(arr)-quater):
            if arr[i]==arr[i+quater]:
                return arr[i]
        return -1
        