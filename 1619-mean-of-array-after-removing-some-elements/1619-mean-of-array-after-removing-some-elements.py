class Solution:
    def trimMean(self, arr: List[int]) -> float:
        #We first need to sort the given array, then we can add up all of the ones in the middle 90% and and divide the sum by the total number of elements within this 90% range and return.
        arr.sort()
        n=len(arr)
        sum=0
        for i in range(int(n*0.05),int(n-0.05*n)):
            sum+=arr[i]
            
        return sum/(n-n*0.1)

        