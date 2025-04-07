/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    // const allSubsets = [];

    function generateSubsetsBacktrack(currIdx, nums){
        // Base Case:
        if(currIdx === nums.length){
            return [[]];
        }

        const nextSubsets = generateSubsetsBacktrack(currIdx + 1, nums);

        const allSubsets = [];
        for(let subset of nextSubsets){
            // [1, 2, 3]
            // [[]] => results [[], [3]] => idx2
            // [[],[3]] => results [[], [2], [3], [2,3]] => idx1
            // [[], [2], [3], [2,3]] => results [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]] => idx1
            allSubsets.push(subset);
            allSubsets.push([nums[currIdx], ...subset]);
        }

        return allSubsets;
    }
    return generateSubsetsBacktrack(0, nums);

    // return allSubsets;
};