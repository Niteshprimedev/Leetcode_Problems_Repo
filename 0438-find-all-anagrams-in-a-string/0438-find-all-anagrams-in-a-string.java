class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> allAnagrams = new ArrayList<>();

        int[] freq = new int[26];

        Arrays.fill(freq, 0);

        for(char curr : p.toCharArray()){
            int charIdx = curr - 'a';

            freq[charIdx] += 1;
        }

        int n = s.length();
        int left = 0;
        int right = 0;

        int totalMatches = 0;

        while(right < n){
            int charIdx = s.charAt(right) - 'a';
            freq[charIdx] -= 1;

            if(freq[charIdx] >= 0){
                totalMatches += 1;
            }

            if((right - left + 1) == p.length()){
                if(totalMatches == p.length()){
                    allAnagrams.add(left);
                }

                int leftIdx = s.charAt(left) - 'a';
                freq[leftIdx] += 1;

                if(freq[leftIdx] > 0){
                    totalMatches -= 1;
                }

                left += 1;
            }

            right += 1;
        }
        
        return allAnagrams;
    }
}