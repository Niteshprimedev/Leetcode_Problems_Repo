class Solution {
    public boolean isSubsequence(String s, String t) {
        int strSIdx = 0;
        int strTIdx = 0;

        while(strTIdx < t.length()){
            if(strSIdx < s.length() && s.charAt(strSIdx) == t.charAt(strTIdx)){
                strSIdx += 1;
            }

            strTIdx += 1;
        }

        if(strSIdx == s.length()) return true;

        return false;
    }
}