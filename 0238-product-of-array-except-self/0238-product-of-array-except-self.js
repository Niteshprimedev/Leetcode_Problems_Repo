/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // Pseudocode;
    // Create a zeroesCount Variable and initialize it with 0
    // Create a totalNumsProduct variable and assign it to the product of all the nums element using reduce method;
    // Update zeroesCount variable value by 1 whenever a zero is encountered in array & keep the 0 value as 1
    // Update zeroesCount variable value by 1 whenever a zero is encountered in array & keep the 0 value as 0
    // Run a for loop through the nums array from index i = 0 to nums.length - 1 value
    // Update the nums[i] value in the array with 0s if the zeroCount is 2
    // Else: Update the nums[i] value in the array with the totalNumsProduct variable divided by variable at i
    // And divide by 0 if the value at i is 0
    // Finally, we will have the product of array except self in the nums array so will return it

    let zeroesCount = 0;
    let totalNumsProduct = nums.reduce((a, b) => {
        if(zeroesCount >= 2){
            zeroesCount++;
            b = 0;
        }
        else if(b === 0){
            zeroesCount++;
            b = 1;
        }
        return a * b;
    }, 1);

    // console.log(totalNumsProduct);

    for(let i = 0; i < nums.length; i++){
        if(zeroesCount >= 2){
            nums[i] = 0;
        }
        else if(zeroesCount === 1){
            let elVal = nums[i] === 0 ? totalNumsProduct : 0;
            nums[i]= elVal;
        }
        else{
            nums[i] = totalNumsProduct / nums[i];
        }
    }
    return nums;
};

/***
    // Psuedocode;
    // Create a totalNumsProduct variable and assign it to the product of all the nums element using reduce method;
    // Check if a or b is 0, then update a & b to 1 to get the total product;
    // Create a variable isNumsZeroElArr and assign it to false
    // Update the isNumsZeroElArr to true if the any of the values are zero
    // Loop through the array and map the non-zero values array by diving the totalNumsProduct by the el to get the product of array except self for that element
    // For the zero values array there will be condition
    // If the value is not zero && isNumsZeroElArr is true then keep the 0, else keep the product of array except the zeroes;
    // Handling the edge cases: When all nums are zero then we used a frequency counter obj to return the same array as output;
    // Create a isNumsZeroElFreqObj variable to keep track of the frequency of 0 in the array
    // Finally, return the mapped array;

    // #BruteForce Solution;
    // Create a numsProductArr variable and initialize it to an empty array
    // Run a loop through the nums.length array from 0 to length value
    // Create a totalProductExceptSelf variable and initialize it to 1
    // Run another for loop that starts from 0 index to the length value
    // Accumulate the product of all the elements in the totalProductExceptSelf variable by keeping a if statement
    // Such that the element at a particular index is not equal to the element available at another for loop's incrementing value
    // Push the totalProductExceptSelf variable value to the numsProductArr
    // Once we are done with both the for loops, we will have the array except self

    console.log("Naive Solution and BIG 0 is N^2");
    let numsProductArr = [];

    for(let i = 0; i < nums.length; i++){
        let totalProductExceptSelf = 1;

        for(let j = 0; j < nums.length; j++){
            if(i !== j){
                totalProductExceptSelf *= nums[j];
            }
        }
        numsProductArr.push(totalProductExceptSelf);
    }

    console.log("To-Do: I need to think a solution to optimize this: Time Taken - 20 m 50 s");
    return numsProductArr;
 */