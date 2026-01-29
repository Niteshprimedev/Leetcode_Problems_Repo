class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int totalNiceSubarrs = 0;
        int prefixSum = 0;

        HashMap<Integer, Integer> prefixSumFreqMap = new HashMap<>();

        prefixSumFreqMap.put(0, 1);

        for(int num : nums){
            prefixSum += num;

            int hashKey = prefixSum - goal;

            if(prefixSumFreqMap.containsKey(hashKey)){
                totalNiceSubarrs += prefixSumFreqMap.get(hashKey);
            }

            int hashValue = prefixSumFreqMap.getOrDefault(prefixSum, 0) + 1;
            prefixSumFreqMap.put(prefixSum, hashValue);
        }

        return totalNiceSubarrs;
    }
}