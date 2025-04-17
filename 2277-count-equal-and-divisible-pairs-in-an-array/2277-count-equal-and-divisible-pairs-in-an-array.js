/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    // Brute Force Solution;
    let countArrPairs = 0;
    for(let idxI = 0; idxI < nums.length; idxI++)  {
        for(let idxJ = idxI + 1; idxJ < nums.length; idxJ++){
            const firstNum = nums[idxI];
            const secondNum = nums[idxJ];

            const areIndicesDivisible = (idxI * idxJ) % k === 0 ? true : false;
            if(firstNum === secondNum && areIndicesDivisible){
                countArrPairs += 1;
            }
        }
    }
    return countArrPairs;
};