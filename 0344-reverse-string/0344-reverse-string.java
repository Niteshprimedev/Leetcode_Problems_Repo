class Solution {
    private void reverseStr(int strtIdx, int endIdx, char[] s){
        // Base Case;
        if(strtIdx >= endIdx){
            return;
        }

        // for(char c : s){
        //     System.out.println(c);
        // }

        char strtChar = s[strtIdx];
        s[strtIdx] = s[endIdx];
        s[endIdx] = strtChar;

        reverseStr(strtIdx + 1, endIdx - 1, s);
    }

    public void reverseString(char[] s) {
        // Recursion solution;
        reverseStr(0, s.length - 1, s);
    }
}