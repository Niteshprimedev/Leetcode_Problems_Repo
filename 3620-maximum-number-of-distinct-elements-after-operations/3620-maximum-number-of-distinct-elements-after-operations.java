class Solution {
    public int maxDistinctElements(int[] nums, int k) {
        Arrays.sort(nums);

        // System.out.println(Arrays.toString(nums));

        int distElsCount = 0;
        int n = nums.length;
        int idxI = 0;
        long prevRangeVal = nums[0] - k;

        while(idxI < n){
            long startRange = nums[idxI] - k;
            long endRange = nums[idxI] + k;

            int freqCount = 1;
            while(idxI + 1 < n && nums[idxI] == nums[idxI + 1]){
                freqCount += 1;
                idxI += 1;
            }

            prevRangeVal = Math.max(prevRangeVal, startRange);
            int currDistVals = 0;

            if(prevRangeVal + (long) freqCount <= endRange){
                prevRangeVal += (long) freqCount;
                currDistVals = freqCount;
            }
            else{
                currDistVals = (int) (endRange - prevRangeVal + 1);
                prevRangeVal = endRange + 1;
            }

            //System.out.println("idxI" + idxI + " prevRangeVal" + prevRangeVal + " res" + currDistVals);

            distElsCount += currDistVals;
            idxI += 1;
        }

        return distElsCount;
    }
}