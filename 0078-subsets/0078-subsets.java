import java.util.*;

class Solution {
    private List<List<Integer>> generateAllSubsets(int currIdx, int[] nums, List<Integer> currSubset){
        List<List<Integer>> allSubsets = new ArrayList<>();

        // Base Case:
        if(currIdx == nums.length){
            allSubsets.add(new ArrayList(currSubset));
            return allSubsets;
        }

        // Pick Case;
        currSubset.add(nums[currIdx]);
        List<List<Integer>> pickCase = generateAllSubsets(currIdx + 1, nums, currSubset);

        // Not Pick Case;
        currSubset.removeLast();
        List<List<Integer>> notPickCase = generateAllSubsets(currIdx + 1, nums, currSubset);

        for(List<Integer> subset : pickCase){
            allSubsets.add(subset);
        }

        for(List<Integer> subset : notPickCase){
            allSubsets.add(subset);
        }

        return allSubsets;
    }

    public List<List<Integer>> subsets(int[] nums) {
        // List<List<Integer>> allSubsets = new ArrayList<>();
        List<Integer> currSubset = new ArrayList<>();

        return generateAllSubsets(0, nums, currSubset);
        // return allSubsets;
    }
}