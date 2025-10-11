class Solution {
    public int maxSubArray(int[] nums) {
        int maxSubArrSum = Integer.MIN_VALUE;
        int currSubArrSum = 0;

        for(int num : nums){
            currSubArrSum = Math.max(num, currSubArrSum + num);

            maxSubArrSum = Math.max(maxSubArrSum, currSubArrSum);
        }

        return maxSubArrSum;
    }
}