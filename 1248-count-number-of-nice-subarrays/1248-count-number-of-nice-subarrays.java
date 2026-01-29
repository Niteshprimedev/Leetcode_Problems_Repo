class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        // int[] binaryNums = new int[nums.length];
        // int i = 0;

        // for(int num : nums){
        //     binaryNums[i] = num % 2;
        //     i += 1;
        // }

        int totalNiceSubarrs = 0;
        int prefixSum = 0;

        HashMap<Integer, Integer> prefixSumFreqMap = new HashMap<>();
        prefixSumFreqMap.put(0, 1);

        for(int num : nums){
            prefixSum += num % 2;

            int hashKey = prefixSum - k;

            if(prefixSumFreqMap.containsKey(hashKey)){
                totalNiceSubarrs += prefixSumFreqMap.get(hashKey);
            }

            int hashValue = prefixSumFreqMap.getOrDefault(prefixSum, 0) + 1;
            prefixSumFreqMap.put(prefixSum, hashValue);
        }

        return totalNiceSubarrs;
    }
}