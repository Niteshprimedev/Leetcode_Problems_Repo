class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        
        int n = bits.length;
        int i = 0;
        boolean oneBitChar = false;

        while(i < n){
            int firstChar = bits[i];

            if(firstChar == 1){
                i += 1;
            }
            else if(firstChar == 0 && i == n - 1){
                oneBitChar = true;
            }

            i += 1;
        }

        return oneBitChar;
    }
}