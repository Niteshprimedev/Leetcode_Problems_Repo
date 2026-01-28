class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if(k < 2) return 0;

        int n = nums.length;
        int totalSubarrsProductLessK = 0;
        int prefixProduct = 1;

        int windowStrtIdx = 0;

        for(int windowEndIdx = 0; windowEndIdx < n; windowEndIdx++){
            int currNum = nums[windowEndIdx];
            prefixProduct *= currNum;

            while(prefixProduct >= k && windowStrtIdx <= windowEndIdx){
                prefixProduct = prefixProduct / nums[windowStrtIdx];
                windowStrtIdx += 1;
            }

            totalSubarrsProductLessK += windowEndIdx - windowStrtIdx + 1;
        }

        return totalSubarrsProductLessK;
    }
}