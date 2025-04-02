/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    // The Linear Time O(N) & Space Complexity O(1) can be applied
    // The idea is to calculate the max of nums[i] - nums[j] in the entire array
    // in linear time
    // And then calculate the max val from idxJ till the end of array in Linear time
    // Finally, put the variables value in the equation to compute the result
    // max(x - y) in O(N) fashion and max(z) in O(N) fashion

    // To calculate the max(x - y) we can use hashmap;
    // x 
    let maxTripletsVal = 0;
    let firstNum = nums[0];
    let secondNum = nums[1];
    let maxFirstTwoNumsDiffVal = firstNum - secondNum;

    firstNum = Math.max(firstNum, secondNum);

    for(let thirdNumIdx = 2; thirdNumIdx < nums.length; thirdNumIdx++){
        // console.log('Before', firstNum, maxFirstTwoNumsDiffVal, maxTripletsVal);

        // Use current number as thirdNum i.e nums[k]
        const thirdNum = nums[thirdNumIdx];
        maxTripletsVal = Math.max(maxTripletsVal, (maxFirstTwoNumsDiffVal * thirdNum));

        // Use current number as secondNum i.e nums[j]
        const secondNum = nums[thirdNumIdx];
        maxFirstTwoNumsDiffVal = Math.max(maxFirstTwoNumsDiffVal, firstNum - secondNum);

        // Use current number as firstNum i.e nums[i]
        const newFirstNum = nums[thirdNumIdx];
        firstNum = Math.max(firstNum, newFirstNum);

        // console.log('After', firstNum, secondNum, thirdNum, maxFirstTwoNumsDiffVal, maxTripletsVal);
    }

    return maxTripletsVal;
};