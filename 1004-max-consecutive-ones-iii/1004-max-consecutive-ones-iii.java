class Solution {
    public int longestOnes(int[] nums, int k) {
        /*
        // Solution 1: For Loop & Sliding Window
        int maxConsOnes = 0;

        int n = nums.length;
        int strtIdx = 0;
        int flipCounts = 0;

        for(int endIdx = 0; endIdx < n; endIdx++){
            if(nums[endIdx] == 0){
                flipCounts += 1;
            }

            if(flipCounts > k){
                flipCounts -= 1 - nums[strtIdx];
                strtIdx += 1;
            }

            maxConsOnes = Math.max(maxConsOnes, endIdx - strtIdx + 1);
        }

        return maxConsOnes;
        */

        // Solution 2: While Loop & Sliding Window;
        int maxConsOnes = 0;

        int n = nums.length;
        int strtIdx = 0;
        int endIdx = 0;
        int flipCount = 0;

        while(endIdx < n){
            if(nums[endIdx] == 0){
                flipCount += 1;
            }

            if(flipCount > k){
                if(nums[strtIdx] == 0){
                    flipCount -= 1;
                }

                strtIdx += 1;
            }

            maxConsOnes = endIdx - strtIdx + 1;
            endIdx += 1;
        }

        return maxConsOnes;
    }
}