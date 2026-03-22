class Solution {
    public List<Integer> majorityElement(int[] nums) {
        /*
        // Solution 1
        int n = nums.length;

        int threshold = n / 3;

        List<Integer> majorityEls = new ArrayList<>();
        HashMap<Integer, Integer> numsFreqMap = new HashMap<>();
        

        for(int num : nums){
            int hashValue = numsFreqMap.getOrDefault(num, 0) + 1;
            numsFreqMap.put(num, hashValue);
        }

        for(Map.Entry<Integer, Integer> entry : numsFreqMap.entrySet()){
            int element = entry.getKey();
            int count = entry.getValue();

            if(count > threshold){
                majorityEls.add(element);
            }
        }

        return majorityEls;
        */

        // Solution 2: Using Moores Alog;
        int n = nums.length;

        int threshold = n / 3;

        int c1_count = 0;
        int c2_count = 0;

        int candidate1 = Integer.MIN_VALUE;
        int candidate2 = Integer.MIN_VALUE;

        for(int num : nums){
            if(c1_count == 0 && num != candidate2){
                candidate1 = num;
                c1_count = 1;
            }
            else if(c2_count == 0 && num != candidate1){
                candidate2 = num;
                c2_count = 1;
            }
            else if(num == candidate1){
                c1_count += 1;
            }
            else if(num == candidate2){
                c2_count += 1;
            }
            else{
                c1_count -= 1;
                c2_count -= 1;
            }
        }

        List<Integer> majorityEls = new ArrayList<>();
        c1_count = 0;
        c2_count = 0;

        for(int num : nums){
            if(num == candidate1){
                c1_count += 1;
            }
            else if(num == candidate2){
                c2_count += 1;
            }
        }

        if(c1_count > threshold){
            majorityEls.add(candidate1);
        }

        if(c2_count > threshold){
            majorityEls.add(candidate2);
        }

        return majorityEls;
    }
}