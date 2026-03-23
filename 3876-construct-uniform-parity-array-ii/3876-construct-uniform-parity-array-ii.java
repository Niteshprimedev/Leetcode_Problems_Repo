class Solution {
    public boolean uniformArray(int[] nums1) {
        boolean isEven = false;
        boolean isOdd = false;

        for(int num : nums1){
            if(num % 2 == 0){
                isEven = true;
            }
            else{
                isOdd = true;
            }
        }

        if(isEven && !isOdd) return true;
        if(!isEven && isOdd) return true;

        // now thinking:
        // even & odd -> odd
        // 2 - 5 => -3
        // even all => even
        // odd all => odd
        // but even & odd => we want odd case only;
        int oddNum = Integer.MAX_VALUE;

        for(int num : nums1){
            if(num % 2 == 1){
                oddNum = Math.min(num, oddNum);
            }
        }

        int[] nums2 = new int[nums1.length];

        for(int i = 0; i < nums1.length; i++){
            nums2[i] = nums1[i];

            if(nums1[i] % 2 == 0){
                nums2[i] = nums1[i] - oddNum;
            }

            if(nums2[i] < 1) return false;
        }

        for(int num : nums2){
            if(num % 2 == 0) return false;
        }

        return true;
    }
}