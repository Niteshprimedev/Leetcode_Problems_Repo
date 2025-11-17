class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        /*
        int distance = -1;
        for(int num : nums){
            if(num == 1 && (distance == -1 || distance >= k)){
                distance = 0;
            }
            else if(num == 1 && distance < k){
                return false;
            }
            else if(num == 0 && distance != -1){
                distance += 1;
            }
            // System.out.println("Hello from it: " + distance);
        }

        return true;
        */

        int prev = (int) -1e9;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                if(i - prev <= k) return false;
                prev = i;
            }
        }
        
        return true;
    }
}