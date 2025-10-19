class Solution {
    public int compress(char[] chars) {
        int finalLen = 0;
        int i = 0;
        int n = chars.length;

        while(i < n){
            int freqCount = 1;

            while((i + 1) < n && chars[i] == chars[i + 1]){
                freqCount += 1;
                i += 1;
            }

            chars[finalLen++] = chars[i];
            i += 1;

            if(freqCount <= 1) continue;

            String revFreqCount = String.valueOf(freqCount);

            for(char currCharDigit : revFreqCount.toCharArray()){
                chars[finalLen++] = currCharDigit;
            }
        }

        return finalLen;
    }
}