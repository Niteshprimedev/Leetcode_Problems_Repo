/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const digitLetterComboArr = [];

    if(digits.length === 0) return digitLetterComboArr;

    const phoneDigitLettersObj = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    };

    function generateCombos(currIdx, currStr, digitLetterComboArr, phoneDigiLetterObj){
        // Base Case:
        if(currStr.length === digits.length){
            digitLetterComboArr.push(currStr);
            return digitLetterComboArr;
            // return [...digitLetterComboArr];
        }

        const digitPhoneLetters = phoneDigiLetterObj[digits[currIdx]];
        let result = digitLetterComboArr;
        digitPhoneLetters.split('').forEach(letter => {
            result = generateCombos(currIdx + 1, currStr + letter, digitLetterComboArr, phoneDigiLetterObj);
        });

        // console.log(result, digitLetterComboArr, 'result');
        // return result;
        return digitLetterComboArr;
    }
    return generateCombos(0, '', digitLetterComboArr, phoneDigitLettersObj);
};