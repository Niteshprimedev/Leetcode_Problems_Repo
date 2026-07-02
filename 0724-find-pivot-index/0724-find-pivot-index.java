class Solution {
    public int pivotIndex(int[] nums) {
        int suffixSum = Arrays.stream(nums).sum();
        int prefixSum = 0;

        for(int idx = 0; idx < nums.length; idx++){
            suffixSum -= nums[idx];

            if(prefixSum == suffixSum){
                return idx;
            }

            prefixSum += nums[idx];
        }

        return -1;
    }
}