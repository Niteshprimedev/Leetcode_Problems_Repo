class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int result = 0;

        for(int num : nums){
            if(num % 2 != 0){
                continue;
            }
            
            result = result | num;
        }

        return result;
    }
}