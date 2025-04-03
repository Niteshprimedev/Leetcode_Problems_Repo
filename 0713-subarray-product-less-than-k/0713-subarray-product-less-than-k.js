/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    // Logic: Simple try to maintain the window of subarray whose
    // elements product is less than the given k
    // How the `rightIdx - leftIdx + 1` formula works?
    // cause it gives us the number of *unique* subarrays ending at "right" index!
    if(k < 2) return 0;

    const numsArrLen = nums.length;
    let totalKSubArrsProduct = 0;
    let prefixProduct = 1;

    let windowStrtIdx = 0;
    let windowEndIdx = 0;

    for(windowEndIdx; windowEndIdx < numsArrLen; windowEndIdx++){
        // Expand the window at the end;
        const currNum = nums[windowEndIdx];
        prefixProduct *= currNum;

        // Shrink the window from the start cause the product is
        // greater than or equal to k
        while(prefixProduct >= k){
            prefixProduct = prefixProduct / nums[windowStrtIdx];
            windowStrtIdx++;
        }
        // compute the unique number of subarrays ending at right index;
        totalKSubArrsProduct += windowEndIdx - windowStrtIdx + 1;
    }
    return totalKSubArrsProduct;

    /** 
    // DP Solution;

    function countSubArrs(currIdx, nums, product){
        // Base Case:
        if(product >= k) return 0;
        if((currIdx >= nums.length) && product < k) return 1;

        product = (product * nums[currIdx]);
        const multiplyIt = countSubArrs(currIdx + 1, nums, product);
        product = (product / nums[currIdx]);
        const skipIt = countSubArrs(currIdx + 1, nums, product);

        return multiplyIt + skipIt;
    }
    countSubArrs(0, nums, 1);
    */
};