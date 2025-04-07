/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const allSubsets = [];

    function generateSubsetsBacktrack(currIdx, currSubset, nums){
        // Base Case:
        if(currIdx === nums.length){
            allSubsets.push([...currSubset]);
            return;
        }

        // const allSubsets = [];

        currSubset.push(nums[currIdx]);
        const subsetsWithCurrEl = generateSubsetsBacktrack(currIdx + 1, currSubset, nums);

        // Backtrack and revert back the changes:
        currSubset.pop();
        const subsetsWithoutCurrEl = generateSubsetsBacktrack(currIdx + 1, currSubset, nums);

        // return allSubsets;
    }
    generateSubsetsBacktrack(0, [], nums);

    return allSubsets;
};