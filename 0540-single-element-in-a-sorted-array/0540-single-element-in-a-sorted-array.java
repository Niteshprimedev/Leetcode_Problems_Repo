class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = nums.length;

        if(n == 1){
            return nums[0];
        }

        int left = 0;
        int right = n - 1;

        // while(left <= right){
        //     int mid = left + (right - left) / 2;

        //     // found the single element;
        //     if((mid > 0 && nums[mid - 1] != nums[mid]) && ((mid + 1) < n && nums[mid + 1] != nums[mid])){
        //         return nums[mid];
        //     }
        //     // Even then go to left; cause odd els at left
        //     if((mid % 2 == 0) && (mid > 0 && nums[mid - 1] == nums[mid])){
        //         right = mid - 1;
        //     }
        //     // Odd then go to right; cause odd els at right
        //     else if((mid % 2 != 0) && ((mid + 1) < n && nums[mid + 1] == nums[mid]){
        //         right = mid - 1;
        //     }
        // }

        while(left <= right){
            int mid = left + (right - left) / 2;

            // found the single element;
            // if single element is at index 0;
            if(mid == 0 && nums[mid] != nums[mid + 1]){
                return nums[mid];
            }
            // if single element is at last index n - 1;
            else if(mid == (n - 1) && nums[mid] != nums[mid - 1]){
                return nums[mid];
            }
            // if single element is at middle index then check both;
            else if(nums[mid - 1] != nums[mid] && nums[mid + 1] != nums[mid]){
                return nums[mid];
            }

            if((mid % 2 == 0) && (mid > 0 && nums[mid] == nums[mid - 1])){
                right = mid - 1;
            }
            else if((mid % 2 != 0) && ((mid + 1) < n && nums[mid] == nums[mid + 1])){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }

        return -1;
    }
}