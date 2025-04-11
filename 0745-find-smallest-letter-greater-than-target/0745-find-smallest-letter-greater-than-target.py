class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        idd=0
        while l<=r:
            m=(l+r)//2
            if letters[m]>target:
                idd=m
                r=m-1
            else:
                l=m+1
        return letters[idd]
        