class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);

        List<List<Integer>> minAbsDiffPairs = new ArrayList<>();
        int minDiff = Integer.MAX_VALUE;
        int n = arr.length;

        for(int i = 0; i < n; i++){
            int newMinDiff = i > 0 ? arr[i] - arr[i - 1] : Integer.MAX_VALUE;

            minDiff = Math.min(minDiff, newMinDiff);
        }

        for(int i = 0; i < n; i++){
            int currDiff = i > 0 ? arr[i] - arr[i - 1] : Integer.MAX_VALUE;

            if(currDiff == minDiff){
                minAbsDiffPairs.add(Arrays.asList(arr[i - 1], arr[i]));
            }
        }

        return minAbsDiffPairs;
    }
}