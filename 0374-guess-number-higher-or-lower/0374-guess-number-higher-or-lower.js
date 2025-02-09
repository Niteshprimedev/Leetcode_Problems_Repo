/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let pickedNum = guess(n);

    if(pickedNum === 0) return n;

    let leftNum = 0;
    let rightNum = n;
    let midNum = leftNum + (rightNum - leftNum) / 2;

    pickedNum = guess(midNum);

    while(leftNum <= rightNum){
        if(pickedNum === 0){
            return midNum;
        }
        else if(pickedNum === 1){
            leftNum = midNum;
        }
        else if(pickedNum === -1){
            rightNum = midNum;
        }
        midNum = leftNum + (rightNum - leftNum) / 2;
        pickedNum = guess(midNum);
    }
};