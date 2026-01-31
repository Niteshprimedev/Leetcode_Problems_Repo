class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char smallestGreaterChar = target;
        int smallestGreaterCharIdx = smallestGreaterChar + 27;

        for(char currChar : letters){
            int charIdx = currChar;
            int targetCharIdx = target;

            // System.out.println(charIdx + " " + targetCharIdx + " " + smallestGreaterCharIdx);

            if(charIdx > targetCharIdx && charIdx < smallestGreaterCharIdx){
                smallestGreaterChar = currChar;
                smallestGreaterCharIdx = smallestGreaterChar;
                // System.out.println("smallest? " + smallestGreaterChar);
            }
        }
        
        return smallestGreaterChar == target ? letters[0] : smallestGreaterChar;
    }
}