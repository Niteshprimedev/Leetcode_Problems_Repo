class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int windowStrtIdx = 0;

        int minSizeTargetSubarrSum = n + 1;
        int currWindowSum = 0;

        for(int windowEndIdx = 0; windowEndIdx < n; windowEndIdx++){
            int currNum = nums[windowEndIdx];

            currWindowSum += currNum;

            while(currWindowSum >= target && windowStrtIdx <= windowEndIdx){
                int windowSize = windowEndIdx - windowStrtIdx + 1;
                minSizeTargetSubarrSum = Math.min(minSizeTargetSubarrSum, windowSize);

                currWindowSum -= nums[windowStrtIdx];
                windowStrtIdx += 1;
            }
        }

        if(minSizeTargetSubarrSum == n + 1){
            return 0;
        }

        return minSizeTargetSubarrSum;
    }
}