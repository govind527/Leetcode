class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force solution
        # res=0
        # for left in range(len(height)):
        #     for right in range(left+1,len(height)):
        #         area=(right-left)*min(height[left],height[right])
        #         res=max(res,area)
        # return res
        #optimal solution
        res=0
        left,right=0,len(height)-1
        while(left<right):
            area=(right-left)*min(height[left],height[right])
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
        return res
            
    

        