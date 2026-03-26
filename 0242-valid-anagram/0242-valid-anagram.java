class Solution {
    public boolean isAnagram(String s, String t) {
        /*
        // Solution 1: Using Two HashMaps & Freq Counter;
        HashMap<Character, Integer> strSFreqMap = new HashMap<>();
        HashMap<Character, Integer> strTFreqMap = new HashMap<>();

        for(char curr : s.toCharArray()){
            strSFreqMap.put(curr, strSFreqMap.getOrDefault(curr, 0) + 1);
        }
      
        for(char curr : t.toCharArray()){
            strTFreqMap.put(curr, strTFreqMap.getOrDefault(curr, 0) + 1);
        }

        if(strSFreqMap.size() != strTFreqMap.size()) return false;

        for(Map.Entry<Character, Integer> entry : strTFreqMap.entrySet()){
            char hashKey = entry.getKey();
            int hashValue = entry.getValue();

            if(strSFreqMap.getOrDefault(hashKey, 0) != hashValue){
                return false;
            }
        }

        return true;
        */

        /*
        // Meta Prep Time Practice
        // Solution 2: Using 1 HashMaps & Freq Counter & Min Window Str Logic;
        if(s.length() != t.length()) return false;

        HashMap<Character, Integer> strSFreqMap = new HashMap<>();

        for(char curr : s.toCharArray()){
            strSFreqMap.put(curr, strSFreqMap.getOrDefault(curr, 0) + 1);
        }
      
        for(char curr : t.toCharArray()){
            int hashValue = strSFreqMap.getOrDefault(curr, -1) - 1;

            if(hashValue > 0){
                strSFreqMap.put(curr, hashValue);
            }
            else if(hashValue == 0){
                strSFreqMap.remove(curr);
            }
            else{
                return false;
            }
        }

        return true;
        */

        // OR:
        if(s.length() != t.length()) return false;
        
        HashMap<Character, Integer> strSFreqMap = new HashMap<>();

        for(char curr : s.toCharArray()){
            strSFreqMap.put(curr, strSFreqMap.getOrDefault(curr, 0) + 1);
        }
      
        for(char curr : t.toCharArray()){
            int hashValue = strSFreqMap.getOrDefault(curr, -1) - 1;

            if(hashValue >= 0){
                strSFreqMap.put(curr, hashValue);
            }
            else{
                return false;
            }
        }

        return true;
    }
}