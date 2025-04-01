/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    // Solution using Binary Search;

    let peakElIdx = -1;

    let leftIdx = 0;
    let rightIdx = nums.length - 1;
    let middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

    while(leftIdx < rightIdx){
        middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

        if(nums[middleIdx] > nums[middleIdx + 1]){
            rightIdx = middleIdx;
        }
        else if(nums[middleIdx] < nums[middleIdx + 1]){
            leftIdx = middleIdx + 1;
        }
    }

    peakElIdx = leftIdx;

    return peakElIdx;
};