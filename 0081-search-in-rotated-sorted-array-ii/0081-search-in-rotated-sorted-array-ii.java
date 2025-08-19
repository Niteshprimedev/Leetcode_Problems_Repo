class Solution {
    public boolean search(int[] nums, int target) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;

        while (left <= right){
            int mid = left + (right - left) / 2;
            System.out.println(left +""+ mid + "" + right);

            int smallerIdx = mid;

            while(smallerIdx > left && nums[smallerIdx - 1] == nums[mid]){
                smallerIdx -= 1;
            }

            // The target is found at middle idx?
            if(nums[mid] == target){
                return true;
            }
            // is the left part is sorted? and the target is present in it?
            else if((nums[left] <= nums[mid] && smallerIdx == left) || (smallerIdx > left && nums[left] <= nums[smallerIdx - 1] && nums[smallerIdx - 1] <= nums[mid])){
                // Is the target present to the left side of array;
                if(nums[left] <= target && target <= nums[mid]){
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
            else{
                // Is the target present to the side of array;
                if(nums[mid] <= target && target <= nums[right]){
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }
            }
        }

        return false;
    }
}