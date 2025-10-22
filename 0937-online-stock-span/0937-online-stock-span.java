class StockSpanner {
    Stack<Integer> prevGreaterStack = new Stack<>();
    Stack<Integer> prevGreaterElsStack = new Stack<>();
    int size = 0;
    int stockIdx = -1;

    public StockSpanner() {

    }
    
    public int next(int price) {
        this.size += 1;
        this.stockIdx += 1;

        int maxStockSpan = this.stockIdx + 1;

        while(!this.prevGreaterStack.isEmpty() && this.prevGreaterElsStack.peek() <= price){
            this.prevGreaterElsStack.pop();
            this.prevGreaterStack.pop();
        }

        if(!this.prevGreaterStack.isEmpty()){
            maxStockSpan = this.stockIdx - this.prevGreaterStack.peek();
        }

        this.prevGreaterElsStack.push(price);
        this.prevGreaterStack.push(stockIdx);

        return maxStockSpan;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */