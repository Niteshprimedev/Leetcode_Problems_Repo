/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function(s, k) {
    // Pseudocode;
    // Solution using Hash table and the Hint Logic i.e Palindromic Pattern
    // Check for edge case and return false if the value of k is greater than the s.length value
    // Otherwise, 
    // Create a strLettersFrequencyHashMap variable and initialize it to an empty hash map
    // Create a totalOddLettersCount variable and initialize it to 0
    // Run a for loop through string s from index i = 0 to index i = s.length - 1 value
    // Update the strLettersFrequencyHashMap with the element of s at index i as key &
    // its frequency as value, if frequency is not present then start with value 1
    // {key: value} key: string s element at index i, value: previous frequency + 1 or 1 to start with
    // Run a forEach through the strLettersFrequencyHashMap and for each letterKey 
    // Increment the totalOddLettersCount value by 1 if the value for that key is odd in hash map
    // Continue the forEach loop and once it's done
    // Finally, we will have be able to determine if the string can construct k possible palindromes or not
    // in the form of boolean value in the totalOddLettersCount variable so will return it;

    // Edge case;
    if(k > s.length) return false;
    
    // Variable & Setup
    const strLettersFrequencyHashMap = new Map();
    let totalOddLettersCount = 0;

    // Fill the Hashmap with the letters frequencies
    for(let i = 0; i < s.length; i++){
        let letterKey = s[i];
        let letterValue = (strLettersFrequencyHashMap.get(letterKey) || 0) + 1;
        strLettersFrequencyHashMap.set(letterKey, letterValue);
    }

    // console.log(strLettersFrequencyHashMap);
    // Find the odd letters count & Increment the value
    strLettersFrequencyHashMap.forEach((letterValue, letterKey) => {
        if(strLettersFrequencyHashMap.get(letterKey) % 2 === 1){
            totalOddLettersCount++;
        }
    });

    // Return true if the odd letters count is less than or equal to k, else return false;
    return totalOddLettersCount <= k;
};