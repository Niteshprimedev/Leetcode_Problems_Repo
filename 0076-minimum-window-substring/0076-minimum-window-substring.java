class Solution {
    public String minWindow(String s, String t) {
        String minSubstr = "";
        int minSubStrLen = s.length() + 1;

        int[] charsFreqMap = new int[256];

        for(char currChar : t.toCharArray()){
            int charIdx = currChar;
            charsFreqMap[charIdx] += 1;
        }

        int totalMatches = 0;
        int strtIdx = 0;

        for(int endIdx = 0; endIdx < s.length(); endIdx++){
            char currChar = s.charAt(endIdx);
            int charIdx = currChar;

            if(charsFreqMap[charIdx] > 0){
                totalMatches += 1;
            }
            charsFreqMap[charIdx] -= 1;

            while(totalMatches == t.length() && strtIdx <= endIdx){
                int windowSize = endIdx - strtIdx + 1;

                if(windowSize < minSubStrLen){
                    minSubStrLen = windowSize;
                    minSubstr = s.substring(strtIdx, endIdx + 1);
                }

                int strtCharIdx = s.charAt(strtIdx);
                charsFreqMap[strtCharIdx] += 1;
                if(charsFreqMap[strtCharIdx] > 0){
                    totalMatches -= 1;
                }

                strtIdx += 1;
            }
        }

        return minSubstr;
    }
}