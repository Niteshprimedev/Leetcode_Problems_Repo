class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder("");

        for(String word : words){
            int currWordWeight = 0;
            for(char currChar : word.toCharArray()){
                int charIdx = currChar - 'a';
                currWordWeight += weights[charIdx];
            }

            int revCharIdx = currWordWeight % 26;
            char wordToChar = (char) (122 - revCharIdx);

            sb.append(wordToChar);
        }

        return sb.toString();
    }
}