class Solution {
    public int addDigits(int num) {
        // return (num - 1) % 9 + 1;

        // Solution 2;
        while(num > 9){
            int nextNum = 0;

            while(num > 0){
                nextNum += (num % 10);
                num /= 10;
            }

            num = nextNum;
        }

        return num;
    }
}