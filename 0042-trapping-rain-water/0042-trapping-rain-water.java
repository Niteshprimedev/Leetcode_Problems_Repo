class Solution {
    public int trap(int[] height) {
        // Two pointers Logic
		int n = height.length;
			
		int leftIdx = 0;
		int rightIdx = n - 1;
		int trappedRainWaterUnits = 0;
		
		int maxLeftBoundary = Integer.MIN_VALUE;
		int maxRightBoundary = Integer.MIN_VALUE;
		
		while(leftIdx < rightIdx){
			maxLeftBoundary = Math.max(maxLeftBoundary, height[leftIdx]);
			maxRightBoundary = Math.max(maxRightBoundary, height[rightIdx]);
			
			if(maxLeftBoundary <= maxRightBoundary){
				trappedRainWaterUnits += maxLeftBoundary - height[leftIdx];
				leftIdx += 1;
			}
			else{
				trappedRainWaterUnits += maxRightBoundary - height[rightIdx];
				rightIdx -= 1;
			}
		}
		
		return trappedRainWaterUnits;
    }
}