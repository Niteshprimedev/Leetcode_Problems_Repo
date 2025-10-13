class Solution {
    public List<String> removeAnagrams(String[] words) {
        int n = words.length;
        List<String> anagramStrings = new ArrayList<>();
        // HashSet<String> uniqueAnagrams = new HashSet<>();
        anagramStrings.add(words[0]);

        for(int i = 1; i < n; i++){
            char[] prevWordChars = words[i - 1].toCharArray();
            char[] currWordChars = words[i].toCharArray();

            Arrays.sort(prevWordChars);
            Arrays.sort(currWordChars);

            String sortedPrevWord = new String(prevWordChars);
            String sortedCurrWord = new String(currWordChars);

            if(!sortedPrevWord.equals(sortedCurrWord)){
                anagramStrings.add(words[i]);
            }
        }

        return anagramStrings;
    }
}