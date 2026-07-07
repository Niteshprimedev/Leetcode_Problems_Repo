class Solution {
    public long sumAndMultiply(int n) {
        int sumX = 0;
        int numX = 0;

        while(n > 0){
            int digit = n % 10;
            sumX += digit;

            if(digit != 0){
                numX = (numX * 10) + digit;
            }

            n = n / 10;
        }

        int revNum = 0;

        while(numX > 0){
            revNum = (revNum * 10) + numX % 10;
            numX = numX / 10;
        }

        return (long) sumX * revNum;
    }
}