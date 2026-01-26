class Solution {
    public int findLHS(int[] nums) {
        // Solution 1: Sorting and Sliding Window;
        Arrays.sort(nums);

        int longestSubseq = 0;
        int strtIdx = 0;
        int n = nums.length;

        for(int endIdx = 0; endIdx < n; endIdx++){
            while(strtIdx < endIdx && nums[endIdx] - nums[strtIdx] > 1){
                strtIdx += 1;
            }

            if(nums[strtIdx] != nums[endIdx]){
                longestSubseq = Math.max(longestSubseq, endIdx - strtIdx + 1);
            }
        }

        return longestSubseq;
    }
}