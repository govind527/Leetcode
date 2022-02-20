#Notes:write out result for num=16 to figure out pattern; res[i] = res[i - offset], where offset is the biggest power of 2 <= I;

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp
        