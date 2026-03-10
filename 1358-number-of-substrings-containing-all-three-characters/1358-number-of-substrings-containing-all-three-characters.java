class Solution {
    public int numberOfSubstrings(String s) {
        /*
        // Logic: 
        // Create a valid window that has 3 chars: abc
        // and then compute the substrings with this window
        // and the remaining substrings with the chars to the right
        // Use formula as: 1 for current and (totalChars - endIdx) for
        // the remaining substrings while shrink the window
        // map does have 3 chars in the curr_window
        // else try to create a window;

        int strtIdx = 0;
        int endIdx = 0;
        int totalSubstrings = 0;

        HashMap<Character, Integer> charsFreqMap = new HashMap<>();

        while(endIdx < s.length()){
            char currChar = s.charAt(endIdx);

            int hashValue = charsFreqMap.getOrDefault(currChar, 0) + 1;
            charsFreqMap.put(currChar, hashValue);

            endIdx += 1;

            while(charsFreqMap.size() == 3){
                totalSubstrings += (s.length() - endIdx) + 1;

                char strtChar = s.charAt(strtIdx);

                hashValue = charsFreqMap.getOrDefault(strtChar, 0) - 1;
                charsFreqMap.put(strtChar, hashValue);

                if(hashValue <= 0){
                    charsFreqMap.remove(strtChar);
                }

                strtIdx += 1;
            }
        }

        return totalSubstrings;
        */

        /*
        // SOlution 2:
        // Counting Substrings formula is minFreqOf(a, b, c) 
        // gives the substrings that can be formed;

        int endIdx = 0;
        int totalSubstrings = 0;

        HashMap<Character, Integer> charsFreqMap = new HashMap<>();

        while(endIdx < s.length()){
            char currChar = s.charAt(endIdx);

            charsFreqMap.put(currChar, endIdx);

            if(charsFreqMap.size() == 3){
                int minIdxVal = endIdx + 1;

                for(int idxVal : charsFreqMap.values()){
                    minIdxVal = Math.min(minIdxVal, idxVal);
                }

                totalSubstrings += 1 + minIdxVal;
            }

            endIdx += 1;
        }

        return totalSubstrings;
        */

        // Solution 3: Using Array DS;
        // Counting Substrings formula is minFreqOf(a, b, c) 
        // gives the substrings that can be formed;

        int n = s.length() + 1;
        int endIdx = 0;
        int totalSubstrings = 0;

        int[] lastSeenIdxMap = new int[3];
        Arrays.fill(lastSeenIdxMap, -1);

        while(endIdx < s.length()){
            char currChar = s.charAt(endIdx);

            if(currChar == 'a'){
                lastSeenIdxMap[0] = endIdx;
            }
            else if(currChar == 'b'){
                lastSeenIdxMap[1] = endIdx;
            }
            else{
                lastSeenIdxMap[2] = endIdx;
            }

            int count = 0;
            int minVal = endIdx + 1;
            for(int elVal : lastSeenIdxMap){
                if(elVal != n){
                    minVal = Math.min(minVal, elVal);
                    count += 1;
                }
                else{
                    break;
                }
            }

            if(count == 3){
                totalSubstrings += 1 + minVal;
            }

            endIdx += 1;
        }

        return totalSubstrings;
    }
}