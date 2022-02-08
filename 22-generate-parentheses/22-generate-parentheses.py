class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open <n
        #only add close paranthesis if close<open
        #valid  IIF open==closed==n
        result = []
        stack = []

        def recursive(open, close):
            if(open == close == n):
                result.append("".join(stack))
                return

            if(open < n):
                stack.append('(')
                recursive(open+1,close)
                stack.pop()

            if(close < open):
                stack.append(')')
                recursive(open,close+1)
                stack.pop()

        recursive(0,0)
        return result
#         stk=[]# this hold paranthesis
#         res=[]#which hold list of vlid paranthesis
#         def backtrack(oppen,close):
            
#             if oppen==close==n:
#                 res.append(''.join(stk))
#                 return
            
#             if(oppen<n):
#                 stk.append('(')
#                 backtrack(oppen+1,close)
#                 stk.pop()
                
#             if close<oppen:
#                 stk.append(')')
#                 backtrack(open,close+1)
#                 stk.pop()
#         backtrack(0,0)
#         return res
                
        