class Solution {
    public int minimumPrefixLength(int[] nums) {
        int prefixIdx = 0;

        for(int i = nums.length - 1; i >= 0; i--){
            if(i > 0 && nums[i] <= nums[i - 1]){
                prefixIdx = i;
                break;
            }
        }

        return prefixIdx;
    }
}