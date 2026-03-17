class Solution {
    public int countCompleteSubarrays(int[] nums) {

        // Step 1: Count total unique elements in the entire array
        // We need every subarray to contain ALL of these
        HashSet<Integer> uniqueNums = new HashSet<>();
        for (int num : nums) {
            uniqueNums.add(num);
        }

        int totalUniqueNums = uniqueNums.size();

        int n = nums.length;
        int count = 0;
        int start = 0;

        // Sliding window frequency map
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for (int end = 0; end < n; end++) {

            // Expand window → include nums[end]
            freqMap.put(nums[end], freqMap.getOrDefault(nums[end], 0) + 1);

            // 🔥 When window becomes COMPLETE (has all unique elements)
            while (freqMap.size() == totalUniqueNums) {

                /*
                 🧠 KEY IDEA (REMEMBER THIS):
                 
                 Current window [start → end] is VALID
                 → It already contains ALL required elements

                 👉 So ANY extension to the right will ALSO be valid
                    [start → end]
                    [start → end+1]
                    [start → end+2]
                    ...
                    [start → n-1]

                 💥 Total such subarrays = (n - end)

                 👉 We count ALL of them in ONE SHOT
                */
                count += (n - end);

                // Now shrink from left to find next possible window
                int freq = freqMap.get(nums[start]) - 1;

                if (freq == 0) {
                    // Removing this element breaks completeness
                    freqMap.remove(nums[start]);
                } else {
                    freqMap.put(nums[start], freq);
                }

                start++; // move window forward
            }
        }

        return count;

        /*
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
        */
        
    }
}