/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
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
};