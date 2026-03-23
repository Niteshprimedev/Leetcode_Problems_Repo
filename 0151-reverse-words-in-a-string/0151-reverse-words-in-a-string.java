class Solution {
    public String reverseWords(String s) {
        int endIdx = s.length() - 1;
        String reversedWordsStr = "";
        int strtIdx = endIdx;

        while(endIdx >= 0){
            char currChar = s.charAt(endIdx);

            if(currChar == ' '){
                endIdx -= 1;
                continue;
            }
            
            strtIdx = endIdx;

            while(strtIdx >= 0 && s.charAt(strtIdx) != ' '){
                strtIdx -= 1;
            }

            String currString = s.substring(strtIdx + 1, endIdx + 1);
            reversedWordsStr += currString + " ";

            endIdx = strtIdx;
        }

        return reversedWordsStr.substring(0, reversedWordsStr.length() - 1);
    }
}