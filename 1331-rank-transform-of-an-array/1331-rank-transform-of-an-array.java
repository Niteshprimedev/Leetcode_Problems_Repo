class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] copiedArr = new int[arr.length];

        for(int i = 0; i < arr.length; i++){
            copiedArr[i] = arr[i];
        }

        Arrays.sort(arr);
        Map<Integer, Integer> rankedMap = new HashMap<>();

        int numRank = 0;
        for(int num : arr){
            if(!rankedMap.containsKey(num)){
                numRank += 1;
            }
            rankedMap.put(num, numRank);
        }

        int[] rankedArr = new int[arr.length];

        for(int i = 0; i < arr.length; i++){
            rankedArr[i] = rankedMap.get(copiedArr[i]);
        }

        return rankedArr;
    }
}