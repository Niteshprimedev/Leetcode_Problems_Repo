class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);

        int minMaxPairSum = Integer.MIN_VALUE;

        int n = nums.length;
        int strtIdx = 0;
        int endIdx = n - 1;

        while(strtIdx < endIdx){
            int newMinMaxPairSum = nums[strtIdx] + nums[endIdx];
            minMaxPairSum = Math.max(minMaxPairSum, newMinMaxPairSum);

            strtIdx += 1;
            endIdx -= 1;
        }

        return minMaxPairSum;
    }
}