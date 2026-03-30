class Solution {
    public boolean checkStrings(String s1, String s2) {
        /*
        // a on 0 & 2 => 
        // b on 0 & 1 => not possible;
        // e on 2 and 1 => not possible;

        // T.C 1 =>
        // abcdba => a on 0 and 5, b on 1 & 4, c on 2, d on 3
        // cabdab => a on 1 & 4, b on 2 & 5, c on 0, d on 3
        HashMap<String, Integer> evenOddCharsFreq = new HashMap<>();

        for(int i = 0; i < s1.length(); i++){
            char curr = s1.charAt(i);
            String hashKey = "odd" + String.valueOf(curr);

            if(i % 2 == 0){
                hashKey = "even" + String.valueOf(curr);
            }

            evenOddCharsFreq.put(hashKey, evenOddCharsFreq.getOrDefault(hashKey, 0) + 1);
        }

        for(int i = 0; i < s2.length(); i++){
            char curr = s2.charAt(i);
            String hashKey = "odd" + String.valueOf(curr);

            if(i % 2 == 0){
                hashKey = "even" + String.valueOf(curr);
            }

            if(!evenOddCharsFreq.containsKey(hashKey)){
                return false;
            }

            int hashValue = evenOddCharsFreq.get(hashKey) - 1;

            evenOddCharsFreq.put(hashKey, hashValue);

            if(hashValue == 0){
                evenOddCharsFreq.remove(hashKey);
            }
        }

        return true;
        */

        // Meta Prep Time Practice:

        // We track frequency separately for:
        // 1. Even index characters
        // 2. Odd index characters
        // Because swapping is only allowed within same parity indices

        int[] evenCharsFreq = new int[26]; // freq of chars at even indices
        int[] oddCharsFreq  = new int[26]; // freq of chars at odd indices

        // Step 1: Count frequencies from s1
        for(int i = 0; i < s1.length(); i++){
            int charIdx = s1.charAt(i) - 'a'; // map 'a' → 0, 'b' → 1, ..., 'z' → 25

            if(i % 2 == 0) {
                evenCharsFreq[charIdx]++; // increment even index character count
            } else {
                oddCharsFreq[charIdx]++;  // increment odd index character count
            }
        }

        // Step 2: Subtract frequencies using s2
        // Idea: If s1 and s2 are valid transformations,
        // all counts should cancel out to zero
        for(int i = 0; i < s2.length(); i++){
            int charIdx = s2.charAt(i) - 'a';

            if(i % 2 == 0) {
                evenCharsFreq[charIdx]--; // remove matching even index char
            } else {
                oddCharsFreq[charIdx]--;  // remove matching odd index char
            }
        }

        // Step 3: Verify all frequencies are zero
        // If any non-zero → mismatch → cannot form s2 from s1
        for(int i = 0; i < 26; i++){
            if(evenCharsFreq[i] != 0 || oddCharsFreq[i] != 0) {
                return false;
            }
        }

        // All counts matched perfectly
        return true;
    }
}