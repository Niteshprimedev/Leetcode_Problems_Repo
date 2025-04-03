/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    // Logic:
    // Compute the Max value for the equation;
    // (x - y) * z = should be max
    // such that xi < yj < zk
    // There are two parts in the equation;
    // (x - y) getting the max (x - y) diff
    // z getting the max(z) value so if we can get these two parts done
    // then we can get the max triplet following the given condition
    // What if we don't have max positive value over all triplets then
    // we can retun 0;

    let maxTripletsVal = 0;
    let firstNum = nums[0];
    let secondNum = nums[1];
    let maxFirstSecondNumsDiff = firstNum - secondNum;

    // update the firstNum to be the max of (firstNum, secondNum)
    firstNum = Math.max(firstNum, secondNum);

    for(let thirdNumIdx = 2; thirdNumIdx < nums.length; thirdNumIdx++){
        const thirdNum = nums[thirdNumIdx];

        // Compute the equation for the current thirdNum;
        const newMaxTripletsVal = (maxFirstSecondNumsDiff * thirdNum);

        // Update the maxTripletsVal so far;
        maxTripletsVal = Math.max(maxTripletsVal, newMaxTripletsVal);

        // Update the current thirdNum to be our secondNum;
        secondNum = thirdNum;
        maxFirstSecondNumsDiff = Math.max(maxFirstSecondNumsDiff, (firstNum - secondNum));

        // Update the current thirdNum to be our max firstNum if its max so far;
        firstNum = Math.max(firstNum, thirdNum);
    }

    return maxTripletsVal;
};