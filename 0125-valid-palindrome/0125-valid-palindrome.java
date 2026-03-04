class Solution {
    private boolean isAlphaNum(char currChar){
        int charVal = currChar;

        if((charVal >= 97 && charVal <= 122) || (charVal >= 65 && charVal <= 90) || (charVal >= 48 && charVal <= 57)){
            return true;
        }

        return false;
    }
    public boolean isPalindrome(String s) {
        int strt = 0;
        int end = s.length() - 1;

        // System.out.println((int) 'a' + " " + (int) 'z' + " " + (int) '9' + " " + (int) 'Z');

        while(strt < end){
            // System.out.println(Character.toLowerCase(s.charAt(strt)));
            if(Character.toLowerCase(s.charAt(strt)) == Character.toLowerCase(s.charAt(end))){
                strt += 1;
                end -= 1;
            }
            else if(s.charAt(strt) == ' ' || !isAlphaNum(s.charAt(strt))){
                strt += 1;
            }
            else if(s.charAt(end) == ' ' || !isAlphaNum(s.charAt(end))){
                end -= 1;
            }
            else{
                return false;
            }
        }

        
        return true;
    }
}