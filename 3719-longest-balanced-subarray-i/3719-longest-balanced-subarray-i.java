class Solution {
    public int longestBalanced(int[] nums) {
        int longestSubarr = 0;

        int strt = 0;
        for(int num : nums){
            HashMap<Integer, Integer> evenMap = new HashMap<>();
            HashMap<Integer, Integer> oddMap = new HashMap<>();

            for(int end = strt; end < nums.length; end++){
                int num2 = nums[end];
                if(num2 % 2 == 0){
                    evenMap.put(num2, 1);
                }
                else{
                    oddMap.put(num2, 1);
                }

                // System.out.println(evenMap.size() + " " + oddMap.size());
                if(evenMap.size() == oddMap.size()){
                    longestSubarr = Math.max(longestSubarr, end - strt + 1);
                }
            }
            strt += 1;
        }

        return longestSubarr;
    }
}