class Solution {

    private static int findPivot(int[] nums, int left, int right){
        int pivotIdx = -1;
        int target = nums[right];

        while(left <= right){
            int midIdx = left + (right - left) / 2;

            if(nums[midIdx] > target){
                pivotIdx = midIdx;
                left = midIdx + 1;
            }
            else if(nums[midIdx] < target){
                right = midIdx - 1;
            }
            else{
                break;
            }
        }

        return pivotIdx;
    }

    private static int findTarget(int[] nums, int left, int right, int target){

        while(left <= right){
            int midIdx = left + (right - left) / 2;

            // System.out.println(midIdx + "" + nums[midIdx] + "" + target);
            if(nums[midIdx] == target){
                return midIdx;
            }
            else if(nums[midIdx] > target){
                right = midIdx - 1;
            }
            else{
                left = midIdx + 1;
            }
        }

        return -1;
    }

    public int search(int[] nums, int target) {
        int n = nums.length;

        int targetIdx = -1;

        int leftIdx = 0;
        int rightIdx = n - 1;

        int pivotIdx = findPivot(nums, leftIdx, rightIdx);

        // System.out.println(pivotIdx);

        if(pivotIdx == rightIdx){
            targetIdx = findTarget(nums, leftIdx, rightIdx, target);
        }
        else{
            targetIdx = findTarget(nums, leftIdx, pivotIdx, target);
            // System.out.println(targetIdx);

            if(targetIdx == -1){
                targetIdx = findTarget(nums, pivotIdx + 1, rightIdx, target);
            }
        }

        // System.out.println(targetIdx);
        return targetIdx;

    }
}