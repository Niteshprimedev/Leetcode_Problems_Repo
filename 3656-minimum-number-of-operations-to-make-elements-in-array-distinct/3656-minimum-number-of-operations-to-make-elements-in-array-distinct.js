/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const arrLen = nums.length;

    const numsElsHashmap = new Map();

    // Assume that no duplicates are found, so 0
    let minNumOfOpsForDistinctArrEls = 0;

    // Traverse the array from the end to the beginning
    for (let currIdxI = arrLen - 1; currIdxI >= 0; currIdxI--) {
        const currNum = nums[currIdxI];

        if (numsElsHashmap.has(currNum)) {
            // Found duplicate, calculate operations based on index modulo 3
            if (currIdxI % 3 === 0) {
                minNumOfOpsForDistinctArrEls += (currIdxI + 3) / 3;
            } else if (currIdxI % 3 === 1) {
                minNumOfOpsForDistinctArrEls += (currIdxI + 2) / 3;
            } else {
                minNumOfOpsForDistinctArrEls += (currIdxI + 1) / 3;
            }
            break;
        } else {
            // Add the element to the map
            numsElsHashmap.set(currNum, currIdxI);
        }
    }

    numsElsHashmap.clear();
    return minNumOfOpsForDistinctArrEls;
};