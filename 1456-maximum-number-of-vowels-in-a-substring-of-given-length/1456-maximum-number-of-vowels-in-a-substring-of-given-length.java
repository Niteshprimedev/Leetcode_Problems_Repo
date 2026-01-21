class Solution {
    private boolean isVowel(char c){
        return "aeiou".indexOf(c) >= 0;
    }

    public int maxVowels(String s, int k) {
        int maxNumOfVowels = 0;
        int currVowelsCount = 0;

        int n = s.length();
        int strStrtIdx = 0;
        int strEndIdx = 0;

        while(strEndIdx < n){
            if(strEndIdx - strStrtIdx + 1 > k){
                if(isVowel(s.charAt(strStrtIdx))){
                    currVowelsCount -= 1;
                }
                strStrtIdx += 1;
            }

            char currChar = s.charAt(strEndIdx);

            if(isVowel(currChar)){
                currVowelsCount += 1;
            }


            maxNumOfVowels = Math.max(maxNumOfVowels, currVowelsCount);
            strEndIdx += 1;
        }

        return maxNumOfVowels;
    }
}