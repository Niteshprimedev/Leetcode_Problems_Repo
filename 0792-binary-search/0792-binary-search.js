/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // Edge Case:
    const numsArrLen = nums.length;
    let leftIdx = 0;
    let rightIdx = numsArrLen - 1;
    let middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

    while(leftIdx < rightIdx){
        middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

        if(nums[middleIdx] >= target){
            rightIdx = middleIdx;
        }
        else{
            leftIdx = middleIdx + 1;
        }
    }

    if(nums[leftIdx] === target) return leftIdx;
    return -1;
};