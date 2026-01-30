class Solution {
    public int longestSubarray(int[] nums) {
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