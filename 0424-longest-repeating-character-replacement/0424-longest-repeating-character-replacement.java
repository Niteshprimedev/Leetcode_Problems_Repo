class Solution {
    public int characterReplacement(String s, int k) {
        int longestSubstrLen = 0;
        int maxCharFreq = 0;
        int windowStrtIdx = 0;
        int[] charsArrMap = new int[26];

        Arrays.fill(charsArrMap, 0);

        for(int windowEndIdx = 0; windowEndIdx < s.length(); windowEndIdx++){
            char currChar = s.charAt(windowEndIdx);

            int charIdx = currChar - 65;

            charsArrMap[charIdx] += 1;
            maxCharFreq = Math.max(maxCharFreq, charsArrMap[charIdx]);
            int totalChars = windowEndIdx - windowStrtIdx + 1;
            int replacedChars = totalChars - maxCharFreq;

            if(replacedChars > k){
                char strtChar = s.charAt(windowStrtIdx);
                int strtCharIdx = strtChar - 65;

                charsArrMap[strtCharIdx] -= 1;
                windowStrtIdx += 1;
            }

            int windowSize = windowEndIdx - windowStrtIdx + 1;
            longestSubstrLen = Math.max(longestSubstrLen, windowSize);
        }

        return longestSubstrLen;
    }
}