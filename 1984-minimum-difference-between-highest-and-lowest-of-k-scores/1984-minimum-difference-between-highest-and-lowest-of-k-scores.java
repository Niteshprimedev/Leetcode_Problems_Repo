class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);

        int minDiff = Integer.MAX_VALUE;
        int n = nums.length;

        for(int i = 0; i < n; i++){
            int newMinDiff = i - k + 1 >= 0 ? nums[i] - nums[i - k + 1] : Integer.MAX_VALUE;
            minDiff = Math.min(minDiff, newMinDiff);
        }

        return minDiff;
        
    }
}