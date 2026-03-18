class Solution {
    public int longestSubarray(int[] nums) {
        // Solution 1: Meta Prep Time Practice
        // Dry Run:
        // [1, 1, 0, 1] => longestSubarrLen
        // strt = 0
        // end = 3
        // flips = 1 
        // longestLen = 3

        // Dry Run:
        // [0, 1, 1, 1, 0, 1, 1, 0, 1] => longestSubarrLen
        // strt = 3
        // end = 8
        // flips = 2
        // longestLen = 5

        int longestSubarrLen = 0;
        
        int n = nums.length;
        int strtIdx = 0;
        int endIdx = 0;
        int zeroesCount = 0;

        while(endIdx < n){
            if(nums[endIdx] == 0){
                zeroesCount += 1;
            }

            if(zeroesCount > 1){

                if(nums[strtIdx] == 0){
                    zeroesCount -= 1;
                }
                strtIdx += 1;
            }

            int windowSize = endIdx - strtIdx;
            longestSubarrLen = Math.max(longestSubarrLen, windowSize);
            endIdx += 1;
        }

        return longestSubarrLen;
    }
}