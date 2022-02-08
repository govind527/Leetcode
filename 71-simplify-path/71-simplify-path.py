class Solution:
    def simplifyPath(self, path: str) -> str:
        stk=[]
        
        for c in path.split('/'):
            
            if c=='..': # If the current component is c "..", then
            # we pop an entry from the stack if it's non-empty
                if stk:
                    stk.pop()
            elif c=='.' or not c:# A no-op for c "." or an empty string
                continue
                     
            else:
                stk.append(c)
        return '/'+'/'.join(stk)       # Stich together all the directory names together

            
        
        