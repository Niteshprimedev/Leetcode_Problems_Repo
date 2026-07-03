class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        /*
        List<List<Integer>> arrsDiff = new ArrayList<>();

        HashSet<Integer> seenSet = new HashSet<>();
        List<Integer> firstList = new ArrayList<>();

        for(int idx = 0; idx < nums1.length; idx++){

            for(int idxJ = 0; idxJ < nums2.length; idxJ++){
                if(nums1[idx] == nums2[idxJ]){
                    seenSet.add(nums2[idxJ]);
                    break;
                }
            }

            if(!seenSet.contains(nums1[idx])){
                seenSet.add(nums1[idx]);
                firstList.add(nums1[idx]);
            }
        }

        arrsDiff.add(firstList);
        firstList = new ArrayList<>();

        for(int idxJ = 0; idxJ < nums2.length; idxJ++){
            if(!seenSet.contains(nums2[idxJ])){
                seenSet.add(nums2[idxJ]);
                firstList.add(nums2[idxJ]);
            }
        }

        arrsDiff.add(firstList);
        return arrsDiff;
        */

        // OR;
        List<List<Integer>> arrsDiff = new ArrayList<>();
        Set<Integer> seenNums1 = new HashSet<>();
        Set<Integer> seenNums2 = new HashSet<>();

        List<Integer> firstList = new ArrayList<>();
        List<Integer> secondList = new ArrayList<>();

        for(int num : nums1){
            seenNums1.add(num);
        }

        for(int num : nums2){
            seenNums2.add(num);
        }

        for(int num : nums1){
            if(!seenNums2.contains(num)){
                seenNums2.add(num);
                firstList.add(num);
            }
        }

        for(int num : nums2){
            if(!seenNums1.contains(num)){
                seenNums1.add(num);
                secondList.add(num);
            }
        }

        arrsDiff.add(firstList);
        arrsDiff.add(secondList);

        return arrsDiff;
    }
}