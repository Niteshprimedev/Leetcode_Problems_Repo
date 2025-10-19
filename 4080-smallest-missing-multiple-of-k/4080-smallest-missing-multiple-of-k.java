import java.util.Collections;

class Solution {
    public int missingMultiple(int[] nums, int k) {
        /*
        Set<Integer> seen = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        int smallestVal = k;
        while(seen.contains(smallestVal)){
            //System.out.println(smallestVal);
            smallestVal += k;
        }

        return smallestVal;
        */

        Arrays.sort(nums);

        int smallestVal = k;

        for(int num : nums){
            if(num % k == 0 && num == smallestVal){
                smallestVal += k;
            }
            else if(num > smallestVal){
                break;
            }
        }

        return smallestVal;
    }
}