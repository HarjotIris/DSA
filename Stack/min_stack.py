class MinStack:

    def __init__(self):
        
        self.minStack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        # Push to min_values if it is empty 
        # or val is smaller or equal to the top
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)
        

    def pop(self) -> None:
        if self.minStack:
            if self.minStack[-1] == self.min_values[-1]:
                self.min_values.pop()
            self.minStack.pop()    

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None
        

    def getMin(self) -> int:
        if self.min_values:
            return self.min_values[-1]
        return None

sol = MinStack()
sol.push(1)
sol.push(2)
sol.push(0)
print(sol.getMin()) # return 0
sol.pop()
print(sol.top())    #return 2
print(sol.getMin()) # return 1
        
