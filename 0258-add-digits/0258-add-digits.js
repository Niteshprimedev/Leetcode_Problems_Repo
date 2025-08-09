/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    // If number is divisible by 9 completely then digital root(ans) is 9,else the digital root is remainder obtained.
    return (num - 1) % 9 + 1;
};