class StockSpanner:

    # Solution 1:
    # Logic: Previous Greater Element
    # Note: I did it without maintaining a price array using els_stack
    # idx_stack and two variables;
    def __init__(self):
        self.prev_greater_stack = []
        self.prev_greater_els_stack = []
        self.size = 0
        self.stock_idx = -1

    def next(self, price: int) -> int:
        self.size += 1
        self.stock_idx += 1

        max_stock_span = -1

        # number of days where my stock was increasing 
        while self.prev_greater_stack and self.prev_greater_els_stack[-1] <= price:
            self.prev_greater_stack.pop()
            self.prev_greater_els_stack.pop()
        
        # the day on which my stock started decreasing 
        if self.prev_greater_stack:
            # calculate the number of consecutive days where stock was increasing
            max_stock_span = self.stock_idx - self.prev_greater_stack[-1]
        else:
            # the stock was increasing throughout from the beginning;
            max_stock_span = self.size
        
        self.prev_greater_stack.append(self.stock_idx)
        self.prev_greater_els_stack.append(price)

        return max_stock_span

    '''
    # Solution2: Updated the conditions: and removed else condition
    # Logic: Previous Greater Element
    # Note: I did it without maintaining a price array using els_stack
    # idx_stack and two variables;
    def __init__(self):
        self.prev_greater_stack = []
        self.prev_greater_els_stack = []
        self.size = 0
        self.stock_idx = -1

    def next(self, price: int) -> int:
        self.size += 1
        self.stock_idx += 1

        max_stock_span = -1

        # number of days where my stock was increasing 
        while self.prev_greater_stack and self.prev_greater_els_stack[-1] <= price:
            self.prev_greater_stack.pop()
            self.prev_greater_els_stack.pop()
        
        # the stock was increasing throughout from the beginning;
        max_stock_span = self.size

        # or the day on which my stock started decreasing 
        if self.prev_greater_stack:
            # calculate the number of consecutive days where stock was increasing
            max_stock_span = self.stock_idx - self.prev_greater_stack[-1]
        
        self.prev_greater_stack.append(self.stock_idx)
        self.prev_greater_els_stack.append(price)

        return max_stock_span
    '''

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)