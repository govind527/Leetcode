class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        n=len(arr)
        if n<=1: return []
        
        ## We sort the array because pairs of elements with the minimum absolute difference will definitely 
        ## be next to each other in the sorted array.
        arr.sort()
        
        min_diff=float("inf")
        ans_pairs=[]
        
        for i in range(1,n):
            
            curr_diff = arr[i]-arr[i-1]
            curr_pair = [ arr[i-1], arr[i]]
            
            if curr_diff < min_diff:
                min_diff = curr_diff
                ans_pairs = [ curr_pair ]
                
            elif curr_diff == min_diff:
                ans_pairs.append( curr_pair )
                
        return ans_pairs
        
        