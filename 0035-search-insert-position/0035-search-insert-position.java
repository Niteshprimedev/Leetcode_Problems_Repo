class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        int leftIdx = 0;
        int rightIdx = n - 1;

        while(leftIdx <= rightIdx){
            int midIdx = leftIdx + (rightIdx - leftIdx) / 2;

            // System.out.println(midIdx);
            if(nums[midIdx] >= target){
                rightIdx = midIdx - 1;
            }
            else{
                leftIdx = midIdx + 1;
            }
        }

        return leftIdx;
    }
}