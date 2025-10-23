class Solution {
    private boolean checkSameDigits(String s){
        if(s.length() == 2){
            if(s.charAt(0) == s.charAt(1)) return true;
            return false;
        }

        StringBuilder sb = new StringBuilder("");

        for(int i = 0; i < s.length() - 1; i++){
            int first = Integer.valueOf(s.charAt(i));
            int second = Integer.valueOf(s.charAt(i + 1));

            int digit = (first + second) % 10;
            sb.append(String.valueOf(digit));
        }

        return checkSameDigits(sb.toString());
    }
    public boolean hasSameDigits(String s) {
        return checkSameDigits(s);
    }
}