import java.util.Arrays;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int[] charsArrMap = new int[256];

        Arrays.fill(charsArrMap, -1);

        int strtIdx = 0;
        int longestSubStrLen = 0;

        for(int endIdx = 0; endIdx < n; endIdx++){
            char currChar = s.charAt(endIdx);
            int charIdx = currChar;

            if(charsArrMap[charIdx] != -1){
                int hashValue = charsArrMap[charIdx];

                if(hashValue + 1 > strtIdx){
                    strtIdx = hashValue + 1;
                }
            }

            charsArrMap[charIdx] = endIdx;

            int windowSize = endIdx - strtIdx + 1;
            longestSubStrLen = Math.max(longestSubStrLen, windowSize);
        }

        return longestSubStrLen;

        /*
        // Solution 2:
        int n = s.length();
        HashMap<Character, Integer> charsMap = new HashMap<>();

        int strtIdx = 0;
        int longestSubStrLen = 0;

        for(int endIdx = 0; endIdx < n; endIdx++){
            char currChar = s.charAt(endIdx);
            int charIdx = currChar;

            if(!charsMap.isEmpty() && charsMap.get(currChar) != null){
                int hashValue = charsMap.get(currChar);

                if(hashValue + 1 > strtIdx){
                    strtIdx = hashValue + 1;
                }
            }

            charsMap.put(currChar, endIdx);

            int windowSize = endIdx - strtIdx + 1;
            longestSubStrLen = Math.max(longestSubStrLen, windowSize);
        }

        return longestSubStrLen;
        */
    }
}