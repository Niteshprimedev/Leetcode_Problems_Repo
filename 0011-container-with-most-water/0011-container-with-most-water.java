class Solution {
    public int maxArea(int[] height) {
        int containerWithMostWater = 0;
        
        int left = 0;
        int right = height.length - 1;

        int maxLeftBoundary = height[left];
        int maxRightBoundary = height[right];

        while(left < right){
            maxLeftBoundary = Math.max(maxLeftBoundary, height[left]);
            maxRightBoundary = Math.max(maxRightBoundary, height[right]);

            int minHeight = Math.min(maxLeftBoundary, maxRightBoundary);
            int maxWidth = right - left;

            int newContainerWithMostWater = minHeight * maxWidth;
            containerWithMostWater = Math.max(containerWithMostWater, newContainerWithMostWater);

            if(maxLeftBoundary <= maxRightBoundary){
                left += 1;
            }
            else{
                right -= 1;
            }
        }

        return containerWithMostWater;
    }
}