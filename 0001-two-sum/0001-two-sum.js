/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Logic: 
    // Sum of two elements = target
    // x + y = target
    // or x = target - y;
    // so while traversing the nums array, if we fix the 
    // value of y at index i and then we can check whether
    // the target - y i.e x exists in map or not

    /** 
    // But to get the same indices, we would need to
    // maintain the same order of the array, we can't change;
    // Sorting & Two Pointers Technique: Assuming that 
    // we just need to find one pair;
    nums.sort((a, b) => a - b);

    let firstNumIdx = 0;
    let secondNumIdx = nums.length - 1;
    const twoSumIndices = new Array(2);

    while(firstNumIdx < secondNumIdx){
        const firstNum = nums[firstNumIdx];
        const secondNum = nums[secondNumIdx];

        const twoNumsSum = firstNum + secondNum;
        if(twoNumsSum === target){
            twoSumIndices[0] = firstNumIdx;
            twoSumIndices[1] = secondNumIdx;
            break;
        }
        else if(twoNumsSum < target){
            firstNumIdx++;
        }
        else{
            secondNumIdx--;
        }
    }

    return twoSumIndices;

    */

    const numsElsHashmap = new Map();
    const twoSumIndices = [];

    for(let idxI = 0; idxI < nums.length; idxI++){
        const hashKey = nums[idxI];
        const hashValue = idxI;

        numsElsHashmap.set(hashKey, hashValue);
    }

    // console.log(numsElsHashmap);

    for(let idxJ = 0; idxJ < nums.length; idxJ++){
        const firstNum = nums[idxJ];

        const secondNumKey = target - firstNum;

        const secondNumIdx = numsElsHashmap.get(secondNumKey) || -1;
        if(secondNumIdx > -1 && idxJ !== secondNumIdx){
            twoSumIndices.push(idxJ);
            twoSumIndices.push(secondNumIdx);
            break;
        }
    }

    return twoSumIndices;
};