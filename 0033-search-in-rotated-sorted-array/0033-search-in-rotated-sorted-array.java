class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;

        int leftIdx = 0;
        int rightIdx = n - 1;

        while(leftIdx <= rightIdx){
            int midIdx = leftIdx + (rightIdx - leftIdx) / 2;

            if(nums[midIdx] == target){
                return midIdx;
            }
            else if(nums[leftIdx] <= nums[midIdx]){
                if(nums[leftIdx] <= target && target <= nums[midIdx]){
                    rightIdx = midIdx - 1;
                }
                else{
                    leftIdx = midIdx + 1;
                }
            }
            else{
                if(nums[midIdx] <= target && target <= nums[rightIdx]){
                    leftIdx = midIdx + 1;
                }
                else{
                    rightIdx = midIdx - 1;
                }
            }
        }

        return -1;
    }
}