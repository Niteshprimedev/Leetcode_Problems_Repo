class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> strSCharsMap = new HashMap<>();
        HashMap<Character, Character> strTCharsMap = new HashMap<>();

        for(int idx = 0; idx < s.length(); idx++){
            char strSChar = s.charAt(idx);
            char strTChar = t.charAt(idx);

            if(strSCharsMap.containsKey(strSChar)){
                char hashValue = strSCharsMap.get(strSChar);
                if(hashValue != strTChar){
                    return false;
                }
            }
            else{
                strSCharsMap.put(strSChar, strTChar);
            }

            if(strTCharsMap.containsKey(strTChar)){
                char hashValue = strTCharsMap.get(strTChar);
                if(hashValue != strSChar){
                    return false;
                }
            }
            else{
                strTCharsMap.put(strTChar, strSChar);
            }
        }

        return true;

        /*
        // Solution 2: Frequency Map 
        // Meta Prep Time Practice
        HashMap<Character, Integer> strSCharsMap = new HashMap<>();
        HashMap<Character, Integer> strTCharsMap = new HashMap<>();

        for(char curr : s.toCharArray()){
            strSCharsMap.put(curr, strSCharsMap.getOrDefault(curr, 0) + 1);
        }

        for(char curr : t.toCharArray()){
            strTCharsMap.put(curr, strTCharsMap.getOrDefault(curr, 0) + 1);
        }

        for(Map.Entry<Character, Integer> entry : strSCharsMap.entrySet()){
            int hashKey = entry.getKey();
            int hashValue = entry.getValue();

            if(strTCharsMap.get(hashKey) != hashValue){

            }
        }

        return true;
        */
    }
}