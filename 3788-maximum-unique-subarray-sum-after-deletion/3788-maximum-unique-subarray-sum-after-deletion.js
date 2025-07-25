/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    /** 
    let maxSubArrSum = -101;
    nums.sort((a, b) => a - b);

    const uniqueNumsSet = new Set();

    for(let num of nums){
        uniqueNumsSet.add(num);
    }
    
    const uniqueNums = [...uniqueNumsSet];

    const uniqueNumsArrLen = uniqueNums.length;

    // console.log(uniqueNums, uniqueNumsArrLen);
    
    let newMaxSubArrSum = 0;
    for(let idxI = uniqueNumsArrLen - 1; idxI >= 0; idxI--){
        const currEl = uniqueNums[idxI];

        if(currEl > 0){
            newMaxSubArrSum += currEl;
            maxSubArrSum = Math.max(newMaxSubArrSum, maxSubArrSum);
            
        }
        else if(currEl <= 0 && maxSubArrSum === -101){
            newMaxSubArrSum += currEl;
            maxSubArrSum = Math.max(newMaxSubArrSum, maxSubArrSum);
            
            break;
        }
        else{
            break;
        }
    }

    return maxSubArrSum;
    */
    
    /**
    // SOLUTION 2: Refactored and Improved lOGIC:
    let maxSubArrSum = 0;
    nums.sort((a, b) => a - b);

    // console.log(nums)
    
    // uniqueNumsSET Is Not required cause
    // we already have elements sorted and we can
    // skip duplicates using adjacent property
    
    // Also, we don't need this newMaxSubArrSum var
    // cause we are already accumulating the sum of all
    // positive elements so any element added would be max;
    for(let idxI = nums.length; idxI >= 0; idxI--){
        const currEl = nums[idxI];

        // SKip Duplicates using adjacent element check;
        if(idxI > 0 && currEl === nums[idxI - 1]){
            continue;
        }

        if(currEl > 0){
            // just add the currEl which postive unique element
            // & no need to take the max, cause this element addition is max
            maxSubArrSum += currEl
        }
        else if(currEl <= 0 && maxSubArrSum === 0){
            // just assign the currEl which max amongst all negative elements
            // & no need to take the max, cause this element is max
            maxSubArrSum = currEl;
            
            break;
        }
        // we don't need this extra else condition
        // cause we are already breaking if we ever
        // encounter the maxEl as a negative number
    }

    return maxSubArrSum;
    */

    // SOLUTION 3: Refactored and Improved lOGIC:
    // Handling the negative case first;
    let maxSubArrSum = 0;
    nums.sort((a, b) => a - b);
    // console.log(nums)

    n = nums.length;

    // just return the last which is max amongst all negative elements
    // if there are no elements greater than 0
    if(nums[n - 1] <= 0){
        maxSubArrSum = nums[n - 1];
        return maxSubArrSum;
    }

    // Also, we don't need this newMaxSubArrSum var
    // cause we are already accumulating the sum of all
    // positive elements so any element added would be max;
    for(let idxI = nums.length; idxI >= 0; idxI--){
        const currEl = nums[idxI];

        // SKip Duplicates using adjacent element check;
        if(idxI > 0 && currEl === nums[idxI - 1]){
            continue;
        }

        if(currEl > 0){
            // just add the currEl which postive unique element
            // & no need to take the max, cause this element addition is max
            maxSubArrSum += currEl
        }
    }

    return maxSubArrSum;
};