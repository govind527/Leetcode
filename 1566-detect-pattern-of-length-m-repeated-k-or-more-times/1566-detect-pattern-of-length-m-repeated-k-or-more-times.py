class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        #Algorithm explained:
# We can build a pattern of length m starting from index 0, and try to find matching consecutive non-overlapping subsequences along the way when we iterate through this array. Whenever we found one, we'll increase the counter by one, if not, we'll just break out of the loop since it needs to be consecutive.


        i=0
        while(i<len(arr)):
            part=arr[i:i+m]
            if part*k==arr[i:i+m*k]:
                return True
            i+=1
        return False
        


        