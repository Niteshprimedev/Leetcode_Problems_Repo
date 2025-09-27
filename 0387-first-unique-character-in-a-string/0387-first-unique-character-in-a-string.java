class Solution {
    public int firstUniqChar(String s) {
        int n = s.length();
        int firstUniqueCharIdx = -1;
        HashMap<Character, Integer> map = new HashMap<>();

        for(char currChar : s.toCharArray()){
            map.put(currChar, map.getOrDefault(currChar, 0) + 1);
        }

        for(int i = 0; i < n; i++){
            int charFreq = map.get(s.charAt(i));

            if(charFreq == 1){
                firstUniqueCharIdx = i;
                break;
            }
        }

        return firstUniqueCharIdx;
    }
}