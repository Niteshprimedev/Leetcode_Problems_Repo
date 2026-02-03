class Solution {
    public boolean isTrionic(int[] nums) {
        /* 
        // Solution 1:
        boolean isPTrue = false;
        boolean isQTrue = false;
        boolean isNTrue = false;
        
        int i = 1;
        int n = nums.length;

        while(i < n){
            // Increasing;
            int p = i;
            while(i < n && nums[i] > nums[i - 1]){
                i += 1;
            }

            if(i > p){
                isPTrue = true;
            }
            // System.out.println(i + " " + isPTrue);

            // Decreasing;
            int q = i;
            while(i < n && nums[i] < nums[i - 1]){
                i += 1;
            }

            if(i > q){
                isQTrue = true;
            }

            // System.out.println(i + " " + isQTrue);

            // Increasing;
            int nextN = i;
            while(i < n && nums[i] > nums[i - 1]){
                i += 1;
            }

            if(i > nextN && i == n) {
                isNTrue = true;
            }
            else{
                break;
            }
            
            // System.out.println(i + " " + isNTrue);
        }

        return (isPTrue && isQTrue && isNTrue);
        */

        // Solution 2:
        boolean isPInc = false;
        boolean isQDec = false;
        boolean isNInc = false;

        int idxJ = 1;
        int n = nums.length;

        for(int i = idxJ; i < n; i++){
            if(nums[idxJ] > nums[idxJ - 1]){
                idxJ += 1;
                isPInc = true;
            }
            else{
                break;
            }
        }

        for(int i = idxJ; i < n; i++){
            if(nums[idxJ] < nums[idxJ - 1]){
                idxJ += 1;
                isQDec = true;
            }
            else{
                break;
            }
        }

        for(int i = idxJ; i < n; i++){
            if(nums[idxJ] > nums[idxJ - 1]){
                idxJ += 1;
                isNInc = true;
            }
            else{
                isNInc = false;
                break;
            }
        }

        return (isPInc && isQDec && isNInc);
    }
}