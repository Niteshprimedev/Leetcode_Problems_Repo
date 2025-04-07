/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    function generateSubsetsBacktrack(currIdx) {
        // \U0001f501 Base Case:
        // When we've considered all elements, return a list with one empty subset.
        // This acts as the building block for combining subsets while backtracking.
        if (currIdx === nums.length) {
            return [[]]; // ➕ base: one empty subset to build from
        }

        // \U0001f9e0 Recursive Step:
        // Get all subsets formed from the remaining elements (currIdx + 1 to end)
        const subsetsFromNext = generateSubsetsBacktrack(currIdx + 1);
        const allSubsets = [];

        // \U0001fa84 For every subset we get from the next step:
        // We do two things —
        // 1. Push it as it is (not picking current element)
        // 2. Create a new subset by including current element (picking it)
        for (const subset of subsetsFromNext) {
            allSubsets.push(subset);                      // ❌ not including current element
            allSubsets.push([nums[currIdx], ...subset]);      // ✅ including current element
        }

        // \U0001f680 Return the complete list of subsets built with and without current element
        return allSubsets;
    }
    return generateSubsetsBacktrack(0);
}