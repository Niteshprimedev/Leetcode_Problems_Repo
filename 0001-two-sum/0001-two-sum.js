/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numsElsHashmap = new Map();
    let twoSumIndices = [];

    for(let firstNumIdx = 0; firstNumIdx < nums.length; firstNumIdx++){
        const firstNumKey = nums[firstNumIdx];
        const hashValue = firstNumIdx;
        const secondNumHashkey = target - firstNumKey;

        const isNumAlreadyPresent = numsElsHashmap.has(secondNumHashkey);
        if(isNumAlreadyPresent){
            const secondNumIdx = numsElsHashmap.get(secondNumHashkey);
            twoSumIndices.push(secondNumIdx);
            twoSumIndices.push(firstNumIdx);
        }
        else{
            numsElsHashmap.set(firstNumKey, hashValue);
        }
    }

    return twoSumIndices;
};