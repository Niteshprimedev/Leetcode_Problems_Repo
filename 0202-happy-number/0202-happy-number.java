import java.util.LinkedHashSet;

class Solution {
    public boolean isHappy(int n) {
        // TreeSet;
        /*
        TreeSet<Integer> seen = new TreeSet<>();

        while(!seen.contains(n)){
            int newDigit = 0;
            seen.add(n);

            while(n > 0){
                int digit = n % 10;
                newDigit += digit * digit;

                n /= 10;
            }

            n = newDigit;
        }

        return n == 1;
        */
        
        // LinkedHashSet solution 
        LinkedHashSet<Integer> seen = new LinkedHashSet<>();

        while(!seen.contains(n)){
            int newDigit = 0;
            seen.add(n);

            while(n > 0){
                int digit = n % 10;
                newDigit += digit * digit;

                n /= 10;
            }

            n = newDigit;
        }

        return n == 1;
    }
}