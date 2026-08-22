class Solution {
    private int getSum(int n){
            int sum = 0;

            while(n > 0){
                int digit = n % 10;

                sum += digit;
                n /= 10;
            }

            return sum;
        }

        private int getProduct(int n){
            int product = 1;

            while(n > 0){
                int digit = n % 10;
                product *= digit;
                
                n /= 10;
            }

            return product;
        }
    public boolean checkDivisibility(int n) {
        int totalSum = getSum(n) + getProduct(n);
        return n % totalSum == 0;
    }
}