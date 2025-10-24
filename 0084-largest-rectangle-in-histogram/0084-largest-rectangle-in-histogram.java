class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        int leftBoundary = -1;
        int rightBoundary = 0;

        Stack<Integer> prevSmallerStack = new Stack<>();

        for(int idx = 0; idx < heights.length; idx++){
            int currHeight = heights[idx];
            rightBoundary = idx;

            while(prevSmallerStack.size() > 0 && heights[prevSmallerStack.peek()] >= currHeight){
                int rectHeight = heights[prevSmallerStack.pop()];
                
                leftBoundary = -1;
                
                if(prevSmallerStack.size() > 0){
                    leftBoundary = prevSmallerStack.peek();
                }

                int rectWidth = rightBoundary - 1 - leftBoundary;

                int newMaxArea = rectHeight * rectWidth;
                maxArea = Math.max(maxArea, newMaxArea);
            }

            prevSmallerStack.push(idx);
        }

        rightBoundary = heights.length;
        while(prevSmallerStack.size() > 0){
            int rectHeight = heights[prevSmallerStack.pop()];
            
            leftBoundary = -1;
            
            if(prevSmallerStack.size() > 0){
                leftBoundary = prevSmallerStack.peek();
            }

            int rectWidth = rightBoundary - 1 - leftBoundary;

            int newMaxArea = rectHeight * rectWidth;
            maxArea = Math.max(maxArea, newMaxArea);
        }

        return maxArea;
    }
}