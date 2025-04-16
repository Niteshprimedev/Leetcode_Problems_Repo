/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    /** 
    // Top Down Approach:
    // \U0001f9e0Logic/Intuition Trying Pick and Not Pick technique using recursion + memoization
    // Top Down - Memoization DP Appraoch

    const lastIdx = nums.length;
    const totalNumsArrSum = nums.reduce((acc, curr) => acc + curr);

    // \U0001f6ab If the total sum is odd, we can’t split it into 2 equal subsets
    if (totalNumsArrSum % 2 !== 0) return false;

    const targetPartitionEqualSumK = totalNumsArrSum / 2;
    const memoMap = new Map();

    // \U0001f501 DFS Function to try out pick / not pick combinations
    function subsetEqualsTargetDFS(currIdx, currSubsetSum, nums) {
        // ✅ Base Case: Found a subset with target sum
        if (currSubsetSum === targetPartitionEqualSumK) return true;

        // \U0001f6ab Base Case: Out of bounds or sum exceeded target
        if (currIdx === lastIdx || currSubsetSum > targetPartitionEqualSumK) return false;

        // \U0001f9fe Memoization key
        const hashKey = `${currIdx}-${currSubsetSum}`;
        if (memoMap.has(hashKey)) return memoMap.get(hashKey);

        // ✅ Pick the current element
        const isPickElEqualsSum = subsetEqualsTargetDFS(currIdx + 1, currSubsetSum + nums[currIdx], nums);

        // \U0001f501 If picking worked, return early
        if (isPickElEqualsSum) return true;

        // ❌ Skip (not pick) the current element
        const isSkipElEqualsSum = subsetEqualsTargetDFS(currIdx + 1, currSubsetSum, nums);

        // \U0001f9e0 Store the result in memoMap
        const isPickElOrNotPickElEqualsSum = isPickElEqualsSum || isSkipElEqualsSum;
        memoMap.set(hashKey, isPickElOrNotPickElEqualsSum);

        return isPickElOrNotPickElEqualsSum;
    }

    return subsetEqualsTargetDFS(0, 0, nums);
    */
    // Bottom Up Approach:
    // \U0001f9e0Logic/Intuition Trying Pick and Not Pick technique using recursion + memoization
    // Bottom Up - Memoization DP Appraoch

    const lastIdx = nums.length;
    const totalNumsArrSum = nums.reduce((acc, curr) => acc + curr);

    // \U0001f6ab If the total sum is odd, we can’t split it into 2 equal subsets
    if (totalNumsArrSum % 2 !== 0) return false;

    const targetPartitionEqualSumK = totalNumsArrSum / 2;
    const memoDP = new Array(targetPartitionEqualSumK + 1).fill(false);
    // Base Case:
    memoDP[0] = true;

    let currSubsetSum = targetPartitionEqualSumK;

    for(let idxI = lastIdx - 1; idxI >= 0; idxI--){
        const currEl = nums[idxI];
        for(let sum = currSubsetSum; sum >= currEl; sum--){
            memoDP[sum] = memoDP[sum] || memoDP[sum - currEl];
        }
    }

    return memoDP[currSubsetSum];
};