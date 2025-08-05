class Solution {
    private static int lowerBound(int[][] intervals, int target){
        int n = intervals.length;

        int left = 0;
        int right = n - 1;
        int insertionIdx = -1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            if(intervals[mid][0] > target){
                right = mid - 1;
            }
            else{
                insertionIdx = mid;
                left = mid + 1;
            }
        }

        return insertionIdx;
    }

    private static int[][] mergedIntervals(int[][] intervals){
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

    public int[][] insert(int[][] intervals, int[] newInterval) {
        int insertionIdx = lowerBound(intervals, newInterval[0]);

        int[][] newIntervals = new int[intervals.length + 1][2];

        for(int idx = 0; idx <= insertionIdx; idx++){
            newIntervals[idx] = intervals[idx];
        }

        newIntervals[insertionIdx + 1] = newInterval;

        for(int idx = insertionIdx + 1; idx < intervals.length; idx++){
            newIntervals[idx + 1] = intervals[idx];
        }

        int[][] mergedIntervals = mergedIntervals(newIntervals);
        return mergedIntervals;
    }
}