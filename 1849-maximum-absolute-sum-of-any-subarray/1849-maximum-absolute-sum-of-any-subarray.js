/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAbsoluteSum = function(nums) {

    /**
    // Logic:
    // To figure out the maxAbsPrefixSum: It can be done by 
    // substracting the minimum prefixSum value from the currPrefixSum
    // To figure out the minAbsPrefixSum: It can be done by 
    // substracting the maximum prefixSum value from the currPrefixSum

    // Finally, get the max value among the minAbsPrefixSum & maxAbsPrefixSum
    // And update the maxAnySubArrAbsSum value accordingly.

    let maxPrefixSum = 0;
    let minPrefixSum = 0;
    let currPrefixSum = 0;
    let maxAnySubArrAbsSum = 0;

    for(let num of nums){
        currPrefixSum += num;

        const maxAbsPrefixSum = Math.abs(currPrefixSum - maxPrefixSum);
        const minAbsPrefixSum = Math.abs(currPrefixSum - minPrefixSum);

        maxAnySubArrAbsSum = Math.max(maxAnySubArrAbsSum, Math.max(maxAbsPrefixSum, minAbsPrefixSum));

        maxPrefixSum = Math.max(maxPrefixSum, currPrefixSum);
        minPrefixSum = Math.min(minPrefixSum, currPrefixSum);
    }

    return maxAnySubArrAbsSum;
    */

    // Logic: Hint 4
    // Using Kadane's Algorithm to find the maxSubArrSum
    // Using Kadane's Algorithm to find the minSubArrSum
    // Return the absolute max sum;

    // Pseudocode:
    // Create a maxSubArrSum variable and initialize it to negative infinity;
    // Create a minSubArrSum variable and initialize it to positive infinity;
    // Create a currSubArrSum variable and initialize it to 0;
    // Run a kadane's algorithm to get the maxSubArrSum
    // Run a kadane's algorithm to get the minSubArrSum
    // Run a for loop through the nums array and for each num el
    // Add the num value to the currSubArrSum value
    // Update the maxSubArrSum value with the maximum value among the 
    // maxSubArrSum & currSubArrSum
    // Reset the currSubArrSum to 0 if the value is less than 0
    // Run a for loop through the nums array and for each num el
    // Add the num value to the currSubArrSum value
    // Update the minSubArrSum value with the minimum value among the 
    // minSubArrSum & currSubArrSum
    // Reset the currSubArrSum to 0 if the value is greater than 0
    // Update the maxSubArrSum value with the absolute of maxSubArrSum
    // Update the minSubArrSum value with the absolute of minSubArrSum
    // Create a maxAnySubArrAbsSum variable and initialize it to the maximum value
    // among the maxSubArrSum & the minSubArrSum
    // Finally, we will have the maximum absolute sum of any subarray in the 
    // maxAnySubArrAbsSum variable so will return it;

    let currSubArrSum = 0;
    let maxSubArrSum = -Infinity
    let minSubArrSum = Infinity
    
    // Kadane's Algorithm to calculate the maximum subArray sum;
    for(let num of nums){
        currSubArrSum += num;

        maxSubArrSum = Math.max(maxSubArrSum, currSubArrSum);

        if(currSubArrSum < 0){
            currSubArrSum = 0;
        }
    }

    // console.log('max', maxSubArrSum);
    // Reset the current sub array sum to 0 to calculate the minimum 
    // sub array sum;
    currSubArrSum = 0;

    // Kadane's Algorithm to calculate the minimum subArray sum;
    for(let num of nums){
        currSubArrSum += num;

        minSubArrSum = Math.min(minSubArrSum, currSubArrSum);

        if(currSubArrSum > 0){
            currSubArrSum = 0;
        }
    }

    // console.log('min', minSubArrSum);

    maxSubArrSum = Math.abs(maxSubArrSum);
    minSubArrSum = Math.abs(minSubArrSum);

    // const maxAnySubArrAbsSum = maxSubArrSum >= minSubArrSum ? maxSubArrSum : minSubArrSum;
    const maxAnySubArrAbsSum = Math.max(maxSubArrSum, minSubArrSum);

    return maxAnySubArrAbsSum;

};