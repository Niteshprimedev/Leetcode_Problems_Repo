class MinStack:
    '''

    def __init__(self):
        self.min_stack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        self.size += 1        

    def pop(self) -> None:
        if(self.size == 0):
            return None
        else:
            self.min_stack.pop()
            self.size -= 1        

    def top(self) -> int:
        if(self.size == 0):
            return None
        else:
            return self.min_stack[self.size - 1]        

    def getMin(self) -> int:
        if(self.size == 0):
            return None
        else:
            return min(self.min_stack)    

    '''

    # Consider min val at each node
    def __init__(self):
        self.min_stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if(self.size == 0):
            self.min_stack.append((val, val))
        else:
            curr_min = min(self.min_stack[-1][1], val)
            self.min_stack.append((val, curr_min))

        self.size += 1        

    def pop(self) -> None:
        if(self.size == 0):
            return None
        else:
            self.min_stack.pop()
            self.size -= 1        

    def top(self) -> int:
        if(self.size == 0):
            return None
        else:
            return self.min_stack[-1][0]        

    def getMin(self) -> int:
        if(self.size == 0):
            return None
        else:
            return self.min_stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()