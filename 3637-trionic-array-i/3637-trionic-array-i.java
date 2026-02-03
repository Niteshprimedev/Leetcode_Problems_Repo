class Solution {
    public boolean isTrionic(int[] nums) {
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
    }
}