/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    nums.sort((a, b) => a - b);
    const allUniquePermutationsArr = [];

    function backtrackPermutations(currIdx, nums){
        // Base Case:
        if(currIdx === (nums.length - 1)){
            allUniquePermutationsArr.push([...nums]);
            return allUniquePermutationsArr;
        }

        const usedSet = new Set();

        // Recursive Case:
        for(let swapIdx = currIdx; swapIdx < nums.length; swapIdx++){

            if(usedSet.has(nums[swapIdx])) continue;

            usedSet.add(nums[swapIdx]);

            // Swap the changes:
            [nums[currIdx], nums[swapIdx]] = [nums[swapIdx], nums[currIdx]];
            backtrackPermutations(currIdx + 1, nums);
            
            // Backtrack and revert Changes:
            [nums[currIdx], nums[swapIdx]] = [nums[swapIdx], nums[currIdx]];
        }

        return allUniquePermutationsArr;

    }
    return backtrackPermutations(0, nums);

    /**
    // Pure Recursion & Backtracking Solution;
    nums.sort((a, b) => a - b);

    function backtrackPermutations(currIdx, nums){
        // Base Case:
        if(currIdx === (nums.length - 1)){
            // We are returning nested array cause later on
            // we will be returning allPermutations from our recursive chain
            // and it would be nested arrays;
            return [[...nums]];
        }

        const allPermutations = [];
        const used = new Set();
        for(let swapIdx = currIdx; swapIdx < nums.length; swapIdx++){
            // if(swapIdx !== currIdx && nums[swapIdx] === nums[currIdx]){
            //     continue;
            // }
            if(used.has(nums[swapIdx])) continue;
            used.add(nums[swapIdx]);

            // Swap the indices elements;
            [nums[currIdx], nums[swapIdx]] = [nums[swapIdx], nums[currIdx]];
            // Here the [[...nums]] will get returned once and then the
            // allPermutations will be returned;
            const nextPermutations = backtrackPermutations(currIdx + 1, nums);

            for(let permutation of nextPermutations){
                allPermutations.push(permutation);
            }

            // Back Track & revert back changes 
            [nums[currIdx], nums[swapIdx]] = [nums[swapIdx], nums[currIdx]];
        }

        console.log(currIdx, allPermutations, used);

        return allPermutations;
    }
    const result = backtrackPermutations(0, nums);

    // console.log(result);
    return result;
    */
};