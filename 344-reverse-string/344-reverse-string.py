class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        while(l<r):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
#         Use two pointers: one starts from the left end, the other starts from the right end, we keep swapping the two elements pointed by the two pointers and keep moving the two pointers towards the middle until they meet.

        