class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        ArrayList<int[]> mergedList = new ArrayList<>();
		
		int[] prevInterval = intervals[0];
		
		for(int idx = 1; idx < intervals.length; idx++){
			int[] currInterval = intervals[idx];
			
			if(prevInterval[1] >= currInterval[0]){
				prevInterval[1] = Math.max(prevInterval[1], currInterval[1]);
			}
			else{
				mergedList.add(prevInterval);
				prevInterval = currInterval;
			}
		}
		
		mergedList.add(prevInterval);
		
		int[][] mergedIntervals = new int[mergedList.size()][];
		
		mergedList.toArray(mergedIntervals);
		return mergedIntervals;
    }
}