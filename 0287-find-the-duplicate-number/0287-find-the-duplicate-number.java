class Solution {
    public int findDuplicate(int[] nums) {
        // Binary Search Solution: On Answer
        // Logic: Counting the numbers <= mid if count
        // is greater than the mid then our ans is mid &
        // go to left else go to right;
        // the reason why our answer is mid cause you tell me
        // how many elements are gonna be <= 3 or any number n?
        // the count should be not more than n right? for 3 there
        // could be just 1, 2, and 3 at max but we found the count
        // more than 3 elements then don't you think we have a repeated
        // number as one of them: could be 1, 2, and 3;
        // so we leverage this idea and try binary Search on answer;

        int n = nums.length;

        int left = 1;
        int right = n;

        while(left <= right){
            int mid = left + (right - left) / 2;
            int elsCount = 0;

            for(int num : nums){
                if(num <= mid){
                    elsCount += 1;
                }
            }

            if(elsCount <= mid){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }

        return left;
    }
}