class Solution {
    public int bitwiseComplement(int n) {
        if(n == 0) return 1;
        
        int complementNum = 0;
        int bitPos = 0;

        while(n > 0){
            int currBit = ((n & 1) ^ 1);

            // System.out.println(currBit);

            if(currBit == 1){
                complementNum |= (currBit << bitPos);
            }

            n = n >> 1;
            bitPos += 1;
        }

        return complementNum;
    }
}