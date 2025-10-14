class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        /*
        if(k == 1){
            return true;
        }

        int[] numsArr = nums.stream().mapToInt(Integer::intValue).toArray();

        int n = numsArr.length;
        int strt = 0;
        int end = 1;
        int incSubarrsCount = 0;
        int gap = 0;

        while(end < n){
            if(numsArr[end] > numsArr[end - 1]){
                gap = 0;
                end += 1;
            }
            else{
                gap += 1;
                strt = end;
                end += 1;
            }
            
            if(end - strt == k){
                incSubarrsCount += 1;
            }
            if(gap == 2){
                gap = 0;
                incSubarrsCount = 0;
            }
            
            if(incSubarrsCount == 2 || end - strt == (k * 2)){
                return true;
            }

            System.out.println(strt + "strt" + " " + end + "end " + incSubarrsCount + " count");
        }

        return false;
        */

        if(k == 1){
            return true;
        }

        int[] numsArr = nums.stream().mapToInt(Integer::intValue).toArray();

        int n = numsArr.length;
        int strt = 0;
        int end = 1;

        while(end < n){
            if(numsArr[end] > numsArr[end - 1]){
                end += 1;
            }
            else{
                strt = end;
                end += 1;
            }

            if(end - strt == k && end - (2 * k) >= 0){
                int prevEnd = strt - 1;
                int count = 1;
                while(count < k && numsArr[prevEnd] > numsArr[prevEnd - 1]){
                    count += 1;
                    prevEnd -= 1;
                }

                if(count == k){
                    return true;
                }
            }
            else if(end - strt == (2 * k)){
                return true;
            }
        }

        return false;
    }
}