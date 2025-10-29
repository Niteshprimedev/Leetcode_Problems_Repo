class Solution {
    public int smallestNumber(int n) {
        /*
        int smallestNum = 0;
        int xoredVal = 0;

        for(int i = 0; i < 32; i++){
            int leftShiftVal = 1 << i;
            xoredVal ^= leftShiftVal;
            smallestNum = (n | xoredVal);

            if((leftShiftVal & n) == 0 && smallestNum >= n){
                break;
            }
        }

        return smallestNum;
        */
        
        int  smallestNum = 0;
        int idx = 0;

        while(true){
            if(smallestNum >= n){
                break;
            }

            int leftShiftVal = idx >> 1;
            smallestNum = (smallestNum | leftShiftVal);
            idx += 1;
        }

        return smallestNum;
    }
}