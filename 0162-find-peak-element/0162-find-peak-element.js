/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    // Binary Search Algo:
    // Logic: An element is always considered to be strictly greater than
    // a neighbor that is outside the array.
    // Brute force solution requires us to perform the linear search
    // and check the left + right element to the current element whether its 
    // greater than its neighbors or not;
    // But here we will try the binary search cause if the middleIdx element is
    // greater than its next element i.e middleIdx + 1 element than we will
    // ignore or discard the elements to the right of the middleIdx + 1
    // else we will ignore the elements to the left of the middleIdx cause its
    // smaller than the middleIdx;

    let peakElIdx = -1;
    let leftIdx = 0;
    let rightIdx = nums.length - 1;
    let middleIdx = Math.floor(leftIdx + (rightIdx - leftIdx) / 2);

    while(leftIdx < rightIdx){
        middleIdx = Math.floor(leftIdx + (rightIdx - leftIdx) / 2);

        if(nums[middleIdx + 1] > nums[middleIdx]){
            leftIdx = middleIdx + 1;
        }
        else{
            rightIdx = middleIdx;
        }
    }

    peakElIdx = leftIdx;
    
    return peakElIdx;
};