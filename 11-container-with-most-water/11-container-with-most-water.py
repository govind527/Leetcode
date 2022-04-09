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
        maxx=0
        l=0
        r=len(height)-1
        while(l<r):
            maxx=max(maxx,min(height[l],height[r])*(r-l))# finding the maximum area
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maxx
    

        
