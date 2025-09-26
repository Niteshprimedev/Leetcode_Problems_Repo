class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int n = intervals.length;

        int minIntervalsCount = 0;
        int[] prevInterval = intervals[0];

        for(int i = 1; i < n; i++){
            int[] currInterval = intervals[i];

            if (prevInterval[1] > currInterval[0]){
                minIntervalsCount += 1;
            }
            else{
                prevInterval = currInterval;
            }
        }

        return minIntervalsCount;
    }
}