/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    // Logic: Trying Pick and Not Pick Technique
    // And a sum hashmap;
    const partitionEqualSubsetSumMemoMap = new Map();
    const lastIdx = nums.length;
    const totalNumsArrSum = nums.reduce((acc, currEl) => acc + currEl);

    if(totalNumsArrSum % 2 !== 0) return false;

    const targetPartitionSumK = totalNumsArrSum / 2;
    const memoMap = new Map();

    function subsetEqualsTargetDFS(currIdx, currSubsetSum, nums){
        // Base Case:
        if(currSubsetSum === targetPartitionSumK) return true;
        if(currIdx === lastIdx || currSubsetSum > targetPartitionSumK){
            return false;
        }

        const hashKey = `${currIdx}-${currSubsetSum}`;
        if(memoMap.has(hashKey)) return memoMap.get(hashKey);

        // Recursive case:
        // including the current element
        currSubsetSum = currSubsetSum + nums[currIdx];
        currIdx = currIdx + 1;
        const isPickElPartitionEqualSum = subsetEqualsTargetDFS(currIdx, currSubsetSum, nums);

        if(isPickElPartitionEqualSum){
            return true;
        }
        // not including the current element; backtrack
        currSubsetSum = currSubsetSum - nums[currIdx - 1];
        const isNotPickElPartitionEqualSum = subsetEqualsTargetDFS(currIdx, currSubsetSum, nums);

        // Store the already explored paths:
        const isPickOrNotPickBool = isPickElPartitionEqualSum || isNotPickElPartitionEqualSum
        memoMap.set(hashKey, isPickOrNotPickBool);
        return isPickOrNotPickBool;
    }
    return subsetEqualsTargetDFS(0, 0, nums);

    /** 
    // Brainstorming;
    // Logic: Trying Pick and Not Pick Technique
    // And a sum hashmap;
    const partitionEqualSubsetSumMemoMap = new Map();
    const lastIdx = nums.length;

    function subsetDFS(currIdx, currSubsetSum, currSubsetEls, nums, hashMap){
        // Base Case:
        if(currIdx === lastIdx){
            const isPartitionSumFound = hashMap.has(currSubsetSum);
            if(isPartitionSumFound){
                const hashValue = hashMap.get(currSubsetSum);
                const totalElsCount = currSubsetEls + hashValue;

                if(totalElsCount === lastIdx) return true;
                return false;
            }
            else{
                hashMap.set(currSubsetSum, currSubsetEls);
                return false;   
            }
        }
        // if(currIdx === lastIdx){
            
        // }

        // Recursive case:
        // including the current element
        currSubsetSum = currSubsetSum + nums[currIdx];
        currIdx = currIdx + 1;
        currSubsetEls = currSubsetEls + 1;
        const isPickElPartitionEqualSum = subsetDFS(currIdx, currSubsetSum, currSubsetEls, nums, hashMap);

        if(isPickElPartitionEqualSum){
            return true;
        }
        // not including the current element; backtrack
        currSubsetSum = currSubsetSum - nums[currIdx - 1];
        currSubsetEls = currSubsetEls - 1;
        const isNotPickElPartitionEqualSum = subsetDFS(currIdx, currSubsetSum, currSubsetEls, nums, hashMap);

        return isPickElPartitionEqualSum || isNotPickElPartitionEqualSum;
    }
    return subsetDFS(0, 0, 0, nums, partitionEqualSubsetSumMemoMap);
    */
};