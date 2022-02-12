class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1# using two pointers and left is buying and right is selling
        maxx=0
        while(right <len(prices)):
            #check if profitable??
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxx=max(maxx,profit)
            else:
                left=right
            right+=1
        return maxx
                
        