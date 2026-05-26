class Solution {
    public int numberOfSpecialChars(String word) {
        int[][] charsArr = new int[26][2];

        for(int[] currRow : charsArr){
            Arrays.fill(currRow, -1);
        }
        
        for(char curr : word.toCharArray()){
            char lowerCase = Character.toLowerCase(curr);
            char upperCase = Character.toUpperCase(curr);

            int charIdx = lowerCase - 'a';
            // System.out.println(charIdx + "" + charIdx + " " + curr);

            if(curr == lowerCase && charsArr[charIdx][0] == -1){
                charsArr[charIdx][0] = 1;
            }
            else if(curr == upperCase){
                charsArr[charIdx][1] = 1;
            }
        }

        int specialCharsCount = 0;

        for(int[] currRow : charsArr){
            boolean isLower = currRow[0] != -1 ? true : false;
            boolean isUpper = currRow[1] != -1 ? true : false;

            if(isLower && isUpper){
                specialCharsCount += 1;
            }
        }

        return specialCharsCount;
    }
}