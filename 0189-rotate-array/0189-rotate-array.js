/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

    // Logic: 
    // When reversing to the right by k steps
    // First need to reverse the entire array,
    // then reverse the first k steps & then the last k steps

    // When reversing to the left by k steps;
    // First need to reverse the first k steps & then last k steps
    // Finally, need to reverse the entire array;
    
    const numsLen = nums.length;
    k = k % numsLen;

    if(k === 0) return nums;

    function reverse(strtIdx, endIdx){
        while(strtIdx < endIdx){
            [nums[strtIdx], nums[endIdx]] = [nums[endIdx], nums[strtIdx]];
            strtIdx++;
            endIdx--;
        }
        return;
    }

    // reverse the entire array;
    reverse(0, numsLen - 1);

    // reverse first k elements;
    reverse(0, k - 1);

    // reverse last k lements;
    reverse(k, numsLen - 1);

    return nums;
};