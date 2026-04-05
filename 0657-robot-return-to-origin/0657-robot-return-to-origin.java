class Solution {
    public boolean judgeCircle(String moves) {
        int lFreq = 0;
        int rFreq = 0;
        int uFreq = 0;
        int dFreq = 0;

        for(char curr : moves.toCharArray()){
            if(curr == 'U'){
                uFreq += 1;
            }
            else if(curr == 'D'){
                dFreq += 1;
            }
            else if(curr == 'L'){
                lFreq += 1;
            }
            else{
                rFreq += 1;
            }
        }

        int roboPos = lFreq - rFreq;

        if(roboPos != 0) return false;

        roboPos = dFreq - uFreq;

        return roboPos == 0;
    }
}