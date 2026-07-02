class Solution {
    public int largestAltitude(int[] gain) {
        int prefixAltitude = 0;
        int highestAltitude = 0;

        for(int currGain : gain){
            prefixAltitude += currGain;
            highestAltitude = Math.max(highestAltitude, prefixAltitude);
        }

        return highestAltitude;
    }
}