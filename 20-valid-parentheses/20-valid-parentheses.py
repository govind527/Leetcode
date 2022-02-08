class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        closetoOpen={"]":"[","}":"{",")":"("}
        
        for id in s:
            if id in closetoOpen:
                if stk and stk[-1]==closetoOpen[id]:#if stack is not empty and current element is equal to peak element of stack then pop the element 
                    stk.pop()
                else:
                    return False
            else:
                stk.append(id)
        return True if not stk else False