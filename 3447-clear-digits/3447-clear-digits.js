/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    // Pseudocode;
    // Create a stack data structure to keep the non-digit chars
    // Loop through the string s and for each digit char
    // Remove one non-digit char from the stack
    // Finally, join the item into a string and return the string;

    const strCharsStack = [];
    let clearDigits = '';

    for(let char of s){
        const isADigitChar = isDigit(char);

        if(isADigitChar){
            strCharsStack.pop();
        }
        else{
            strCharsStack.push(char);
        }
    }

    function isDigit(char){
        const newRegxp = new RegExp('^[0-9]$');
        return newRegxp.test(char);
    }

    clearDigits = strCharsStack.join('');
    return clearDigits;
};