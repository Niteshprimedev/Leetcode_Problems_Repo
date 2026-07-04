class Solution {
    public boolean closeStrings(String word1, String word2) {
        // Meta Prep Time Solution 1:
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        for(char curr : word1.toCharArray()){
            freq1[curr - 'a'] += 1;
        }

        for(char curr : word2.toCharArray()){
            freq2[curr - 'a'] += 1;
        }

        // Check if character is present or not?
        for(int i = 0; i < 26; i++){
            boolean isW1CharPresent = freq1[i] == 0;
            boolean isW2CharPresent = freq2[i] == 0;

            if(isW1CharPresent != isW2CharPresent){
                return false;
            }
        }

        // Check equal frequencies;
        Arrays.sort(freq1);
        Arrays.sort(freq2);

        for(int i = 0; i < 26; i++){
            if(freq1[i] != freq2[i]){
                return false;
            }
        }

        return true;
    }
}