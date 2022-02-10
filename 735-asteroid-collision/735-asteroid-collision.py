class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for a in asteroids:
            while stk and a<0 and stk[-1]>0:
                diff= a+stk[-1]
                if diff<0:
                    stk.pop()
                elif diff>0:
                    break #it's mean i have destroy the current astroid
                else:
                        # its mean  have to destroy both astroid
                    stk.pop()
                    break
            else:
                stk.append(a)
        return stk
        