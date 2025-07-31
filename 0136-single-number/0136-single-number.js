/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let numberObj = {}
    for (let val of nums){
        numberObj[val] = (numberObj[val] || 0) + 1;
    }

    for (let numKey in numberObj) {
        if(numberObj[numKey] === 1) {
            return +numKey;
        }
    }
};