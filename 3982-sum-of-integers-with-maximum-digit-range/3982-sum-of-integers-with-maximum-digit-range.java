class Solution {
    private int getDigitRange(int num){
        int maxNum = 0;
        int minNum = num;

        while(num > 0){
            int digit = num % 10;

            maxNum = Math.max(maxNum, digit);
            minNum = Math.min(minNum, digit);

            num = num / 10;
        }

        return maxNum - minNum;
    }

    public int maxDigitRange(int[] nums) {
        int maxDigitRange = -1;
        int allIntSum = 0;

        for(int num : nums){
            int currMax = getDigitRange(num);

            if(currMax > maxDigitRange){
                maxDigitRange = currMax;
                allIntSum = num;
            }
            else if(currMax == maxDigitRange){
                allIntSum += num;
            }
        }

        return allIntSum;
    }
}