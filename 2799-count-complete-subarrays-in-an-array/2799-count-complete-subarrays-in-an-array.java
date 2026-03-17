class Solution {
    public int countCompleteSubarrays(int[] nums) {
        // Number of unique elements in the entire array
        HashSet<Integer> uniqueNums = new HashSet<>();

        for(int num : nums){
            uniqueNums.add(num);
        }

        int totalUniqueNums = uniqueNums.size();
        int n = nums.length;
        int completeSubarrsCount = 0;
        int strt = 0;

        // Frequency map of elements in the current window
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        // [1, 3, 1, 2, 2]
        // 3
        // 1 3 1 2 => 3 then 1, 2
        // 
        for(int end = 0; end < n; end++){
            freqMap.put(nums[end], freqMap.getOrDefault(nums[end], 0) + 1);

            // Shrink the window from strt while it still contains all unique elements
            while(totalUniqueNums == freqMap.size()){
                // All subarrs starting from strt to end till end are valid;
                completeSubarrsCount += n - end;

                int hashValue = freqMap.get(nums[strt]) - 1;

                if(hashValue == 0){
                    freqMap.remove(nums[strt]);
                }
                else{
                    freqMap.put(nums[strt], hashValue);
                }

                strt += 1;
            }
        }

        return completeSubarrsCount;
    }
}