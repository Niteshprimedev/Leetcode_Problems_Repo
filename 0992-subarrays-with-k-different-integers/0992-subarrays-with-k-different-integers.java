class Solution {
    private int countSubarrs(int[] nums, int target){
        if(target <= 0){
            return 0;
        }

        int windowStrtIdx = 0;
        int totalSubarrsCount = 0;

        HashMap<Integer, Integer> numsElsMap = new HashMap<>();

        for(int windowEndIdx = 0; windowEndIdx < nums.length; windowEndIdx++){
            int currNum = nums[windowEndIdx];

            int hashValue = numsElsMap.getOrDefault(currNum, 0);
            numsElsMap.put(currNum, hashValue + 1);

            while(numsElsMap.size() > target && windowStrtIdx <= windowEndIdx){
                int strtNum = nums[windowStrtIdx];

                hashValue = numsElsMap.get(strtNum);

                if(hashValue - 1 == 0){
                    numsElsMap.remove(strtNum);
                }
                else{
                    numsElsMap.put(strtNum, hashValue - 1);
                }

                windowStrtIdx += 1;
            }

            totalSubarrsCount += (windowEndIdx - windowStrtIdx + 1);
        }

        return totalSubarrsCount;
    }
    public int subarraysWithKDistinct(int[] nums, int k) {
        int totalSubarrsSmallerAndEqualK = countSubarrs(nums, k);
        int totalSubarrsSmallerK = countSubarrs(nums, k - 1);

        return totalSubarrsSmallerAndEqualK - totalSubarrsSmallerK;
    }
}