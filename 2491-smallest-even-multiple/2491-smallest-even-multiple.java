class Solution {
    public int smallestEvenMultiple(int n) {
        /*
        if(n % 2 == 0){
            return n;
        }

        return n * 2;
        */

        // Sol2: Bit Manipulation Solution;
        if((n & 1) == 0){
            return n;
        }

        return n * 2;
    }
}