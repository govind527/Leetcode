class MinStack:

    def __init__(self):
        self.stk=[]# this will store original element
        self.minstk=[]# it store only minimum element yet
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        val=min(val,self.minstk[-1] if self.minstk else val) # append this value to minstack only if it is less than the previous element
        self.minstk.append(val)
        

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()