class Solution {
    public int minimumOperations(int[] nums) {
        int minOps = 0;

        for(int num : nums){
            if(num % 3 != 0){
                minOps += 1;
            }
        }   

        return minOps;
    }
}