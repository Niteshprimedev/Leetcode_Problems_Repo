class Solution {
    public int findFinalValue(int[] nums, int original) {
        // HashSet<Integer> numsSet = new HashSet<>(nums);
        // HashSet<Integer> numsSet = Arrays.stream(nums)
        //                             .boxed()
        //                             .collect(Collectors.toSet());

        Set<Integer> numsSet = Arrays.stream(nums)
                                 .boxed()
                                 .collect(Collectors.toSet());


        int result = original;

        while(numsSet.contains(result)){
            result = result * 2;
        }

        return result;
    }
}