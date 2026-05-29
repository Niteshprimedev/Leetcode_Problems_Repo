class Solution {
    public int minElement(int[] nums) {
        int minElVal = 10001;

        for(int num : nums){
            int currMinVal = 0;

            while(num > 0){
                int digit = num % 10;
                currMinVal += digit;

                num = num / 10;
            }

            minElVal = Math.min(minElVal, currMinVal);
        }

        return minElVal;
    }
}