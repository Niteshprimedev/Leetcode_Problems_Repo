class Solution {
    public boolean checkStrings(String s1, String s2) {
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
    }
}