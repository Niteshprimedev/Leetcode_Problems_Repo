class Solution {
    public int longestOnes(int[] nums, int k) {
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