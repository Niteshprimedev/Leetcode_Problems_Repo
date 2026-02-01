class Solution {
    public int minimumCost(int[] nums) {
        int minSubarrsCost = nums[0];
        nums[0] = 0;

        Arrays.sort(nums);

        int count = 0;

        for(int num : nums){
            if(num == 0) continue;

            minSubarrsCost += num;
            count += 1;

            if(count == 2){
                break;
            }
        }

        return minSubarrsCost;
    }
}