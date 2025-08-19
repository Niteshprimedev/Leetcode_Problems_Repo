class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;

        int minVal = Integer.MAX_VALUE;

        while (left <= right){
            int mid = left + (right - left) / 2;

            int smallerIdx = mid;

            while(smallerIdx > left && nums[smallerIdx - 1] == nums[mid]){
                smallerIdx -= 1;
            }

            // is the left part is sorted? and the target is present in it?
            if((nums[left] <= nums[mid] && smallerIdx == left) || (smallerIdx > left && nums[left] <= nums[smallerIdx - 1] && nums[smallerIdx - 1] <= nums[mid])){
                minVal = Math.min(minVal, nums[left]);
                left = mid + 1;
            }
            else{
                minVal = Math.min(minVal, nums[mid]);
                right = mid - 1;
            }
        }

        return minVal;
    }
}