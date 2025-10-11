class Solution {
    private boolean allCardMatches(int sIdx, int pIdx, String s, String p, Boolean[][] memoDP){
        // Base Case:
        if(sIdx == 0 && pIdx == 0){
            return true;
        }
        else if(pIdx == 0) return false;
        else if(sIdx == 0){
            // String is empty, pattern must be all '*'
            for (int i = 0; i < pIdx; i++) {
                if (p.charAt(i) != '*') return false;
            }
            return true;
        }

        if(memoDP[sIdx][pIdx] != null){
            return memoDP[sIdx][pIdx];
        }

        boolean matchCase = false;
        boolean notMatchCase = false;
        if(s.charAt(sIdx - 1) == p.charAt(pIdx - 1)){
            matchCase = allCardMatches(sIdx - 1, pIdx - 1, s, p, memoDP);
        }
        else if(p.charAt(pIdx - 1) == '?'){
            matchCase = allCardMatches(sIdx - 1, pIdx - 1, s, p, memoDP) || matchCase;
        }
        else if(p.charAt(pIdx - 1) == '*'){
            boolean emptyCase = allCardMatches(sIdx, pIdx - 1, s, p, memoDP);
            boolean seqCase = allCardMatches(sIdx - 1, pIdx, s, p, memoDP);

            notMatchCase = emptyCase || seqCase;
        }

        memoDP[sIdx][pIdx] = matchCase || notMatchCase;
        return memoDP[sIdx][pIdx];
    }

    public boolean isMatch(String s, String p) {
        int sLen = s.length();
		int pLen = p.length();
		
		Boolean[][] memoDP = new Boolean[sLen + 1][pLen + 1];

        return allCardMatches(sLen, pLen, s, p, memoDP);		

        // Bottom Up Approach:
        
    }
}