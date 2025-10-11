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
        /*
        int sLen = s.length();
		int pLen = p.length();
		
		Boolean[][] memoDP = new Boolean[sLen + 1][pLen + 1];

        return allCardMatches(sLen, pLen, s, p, memoDP);	
        */	

        // Bottom Up Approach:
        int sLen = s.length();
        int pLen = p.length();

        boolean[][] memoDP = new boolean[sLen + 1][pLen + 1];

        // Base Case:
        memoDP[0][0] = true;

        for(int j = 1; j <= pLen; j++){
            // String is empty, pattern must be all '*'
            boolean allMatches = true;
            for (int k = 0; k < j; k++) {
                if (p.charAt(k) != '*'){
                    allMatches = false;
                    break;
                }
            }
            memoDP[0][j] = allMatches;
        }

        for(int sIdx = 1; sIdx <= sLen; sIdx++){
            for(int pIdx = 1; pIdx <= pLen; pIdx++){
                boolean matchCase = false;
                boolean notMatchCase = false;

                if(s.charAt(sIdx - 1) == p.charAt(pIdx - 1)){
                    matchCase = memoDP[sIdx - 1][pIdx - 1];
                }
                else if(p.charAt(pIdx - 1) == '?'){
                    matchCase = memoDP[sIdx - 1][pIdx - 1] || matchCase;
                }
                else if(p.charAt(pIdx - 1) == '*'){
                    boolean emptyCase = memoDP[sIdx][pIdx - 1];
                    boolean seqCase = memoDP[sIdx - 1][pIdx];

                    notMatchCase = emptyCase || seqCase;
                }

                memoDP[sIdx][pIdx] = matchCase || notMatchCase;
            }
        }
        
        return memoDP[sLen][pLen];
    }
}