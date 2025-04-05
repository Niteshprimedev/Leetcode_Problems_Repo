/**
 * @param {number[]} nums
 * @return {number}
 */
var getLargestOutlier = function(nums) {

    //   n - 2 elements are special numbers
    //   one of the remaining two elements is the sum;
    //   And the second is outlier

    // Equation to Solve:
    // totalArrSum = 2 * (specialNumsSum) + Outlier;
    // So Outlier = totalArrSum - 2 * (specialNumsSum);
    // So the sumOfSpecialNums will be equal to the sum of 1 num;
    // And if we consider that num to be one of the elements in arr
    // while traversing then we can easily calculate the Outlier;

    const numsElsHashmap = new Map();
    let largestPotOutlier =  -Infinity;

    let numIdx = 0;
    for(let num of nums){
        const hashKey = num;
        const hashValue = numIdx;

        numsElsHashmap.set(hashKey, hashValue);
        numIdx++;
    }    

    // console.log(numsElsHashmap);

    const numsArraySum = nums.reduce((acc, currEl) => acc + currEl);

    // console.log(numsArraySum);

    for(let idxI = 0; idxI < nums.length; idxI++){
        const specialNumsSum = nums[idxI];

        const newLargestPotOutlier = numsArraySum - (2 * specialNumsSum);

        const isOutlierPresent = numsElsHashmap.has(newLargestPotOutlier) === true;
        if(isOutlierPresent){
            const newLargestPotOutlierIdx = numsElsHashmap.get(newLargestPotOutlier);
            if(newLargestPotOutlierIdx !== idxI){
                largestPotOutlier = Math.max(largestPotOutlier, newLargestPotOutlier);
            }
        }
    }

    return largestPotOutlier;
    
    /**
    // Brute Force Solution or Backtracking Solution;
    // Just works for these types of inputs & not for -900 900 inputs;
    // [2,3,5,10]
    // [-2,-1,-3,-6,4]
    // [1,1,1,1,1,5,5]
    const numsElsHashmap = new Map();

    let numIdx = 0;
    for(let num of nums){
        const hashKey = num;
        const hashValue = numIdx;

        numsElsHashmap.set(hashKey, hashValue);
        numIdx++;
    }    

    // console.log(numsElsHashmap);

    const numsArraySum = nums.reduce((acc, currEl) => acc + currEl);

    const specialNumsCount = nums.length - 2;
    const numsArrLen = nums.length;

    function subSeqSums(currIdx, totalElsCount, nums, currSum, hashMap, specialNumsSum){
        // Base Case:
        if(totalElsCount >= specialNumsCount){
            console.log(currSum, 'currSum');
            const isCurrSumPresent = hashMap.has(currSum) === true;
            if(isCurrSumPresent){
                specialNumsSum[0] = currSum;
                return true;
            }
            else{
                return false;
            }
            // return 0;
        }

        // include the current element;
        const inlcudeElsLeftSum = subSeqSums(currIdx + 1, totalElsCount + 1, nums, currSum + nums[currIdx], hashMap, specialNumsSum);
        if(inlcudeElsLeftSum){
            return specialNumsSum[0];
        }

        // No More elements can be skipped or not picked;
        let notIncludeElsRightSum = -Infinity;
        if((numsArrLen - currIdx) >= specialNumsCount){
            notIncludeElsRightSum = subSeqSums(currIdx + 1, 0, nums, currSum, hashMap, specialNumsSum);
        }

        if(notIncludeElsRightSum){
            return specialNumsSum[0];
        }

        return false;
    }
    const specialNumsSum = subSeqSums(0, 0, nums, 0, numsElsHashmap, [0]);

    // console.log(specialNumsSum);
    let largestPotOutlier = numsArraySum - (2 * specialNumsSum);

    return largestPotOutlier;
    */
};