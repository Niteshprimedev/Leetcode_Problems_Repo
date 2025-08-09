class Solution {
    int countDigits(int groupSize){
        int totalDigits = 0;
        if(groupSize == -1){
            return totalDigits;
        }

        while (groupSize > 0){
            totalDigits += 1;
            groupSize /= 10;
        }

        return totalDigits;
    }

    public int compress(char[] chars) {
        int groupStrtIdx  = 0;
        int groupEndIdx = 1;
        int compressedStrIdx = 0;

        for(; groupEndIdx <= chars.length; groupEndIdx++){
            if(groupEndIdx == chars.length || chars[groupEndIdx] != chars[groupStrtIdx]){
                int groupSize = groupEndIdx - groupStrtIdx;

                chars[compressedStrIdx++] = chars[groupStrtIdx];

                if(groupSize > 1){
                    int totalDigits = countDigits(groupSize);
                    int idx = totalDigits;

                    while(groupSize > 0){
                        int currDigit = groupSize % 10;
                        chars[compressedStrIdx + totalDigits - 1] = Integer.toString(currDigit).charAt(0);

                        totalDigits -= 1;
                        groupSize /= 10;
                    }

                    compressedStrIdx += idx;
                }

                groupStrtIdx = groupEndIdx;
            }

        }

        return compressedStrIdx;
    }
}