
/**
 * Function to return all possible letter combinations 
 * that the number string could represent based on the 
 * traditional mobile keypad mapping.
 * 
 * @param {string} digits - Input string consisting of digits from 2 to 9
 * @returns {string[]} - All possible letter combinations
 */
 
var letterCombinations = function(digits) {
    const allCombinations = [];

    // Edge Case: Return empty array if no digits are provided
    if (digits.length === 0) return allCombinations;

    // Mapping from digits to corresponding letters on a phone keypad
    const digitToLettersMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    };

    /**
     * Recursive helper function to generate combinations
     * 
     * @param {number} currIdx - Current position in the digits string
     * @param {string} currStrCombo - Current combination being built
     */
    function backtrackCombos(currIdx, currStrCombo) {
        // Base Case: If the combination length matches digits length, store it
        if (currStrCombo.length === digits.length) {
            allCombinations.push(currStrCombo);
            return;
        }

        // Get the letters that the current digit can represent
        const currentDigit = digits[currIdx];
        const possibleLetters = digitToLettersMap[currentDigit];

        // Try each letter and recurse to the next digit
        for (let letter of possibleLetters) {
            backtrackCombos(currIdx + 1, currStrCombo + letter);
        }
    }

    // Kick off the recursion from the first digit
    backtrackCombos(0, '');
    return allCombinations;
};