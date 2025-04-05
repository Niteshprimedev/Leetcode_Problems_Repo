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

    let digitIdx = 0;
    const firstDigit = digits[digitIdx];
    const  firstDigitLetters = phoneDigitLettersObj[firstDigit];

    const isDigitsLenOne = digits.length === 1 ? true : false;
    const isDigitsLenTwo = digits.length === 2 ? true : false;
    const isDigitsLenThree = digits.length === 3 ? true : false;

    for(let firstIdx = 0; firstIdx < firstDigitLetters.length; firstIdx++){
        if(isDigitsLenOne){
            const combo = firstDigitLetters[firstIdx];
            digitLetterComboArr.push(combo);
        }
        digitIdx = 1;
        if(digitIdx < digits.length){
            const secondDigit = digits[digitIdx];
            const  secondDigitLetters = phoneDigitLettersObj[secondDigit];

            for(let secondIdx = 0; secondIdx < secondDigitLetters.length; secondIdx++){
                if(isDigitsLenTwo){
                    const combo = firstDigitLetters[firstIdx] + secondDigitLetters[secondIdx];
                    digitLetterComboArr.push(combo);
                }
                digitIdx = 2;
                if(digitIdx < digits.length){
                    const thirdDigit = digits[digitIdx];
                    const  thirdDigitLetters = phoneDigitLettersObj[thirdDigit];

                    for(let thirdIdx = 0; thirdIdx < thirdDigitLetters.length; thirdIdx++){
                        if(isDigitsLenThree){
                            const combo = firstDigitLetters[firstIdx] + secondDigitLetters[secondIdx] + thirdDigitLetters[thirdIdx];
                            digitLetterComboArr.push(combo);
                        }
                        digitIdx = 3;
                        if(digitIdx < digits.length){
                            const fourthDigit = digits[digitIdx];
                            const  fourthDigitLetters = phoneDigitLettersObj[fourthDigit];

                            for(let fourthIdx = 0; fourthIdx < fourthDigitLetters.length; fourthIdx++){
                                const combo = firstDigitLetters[firstIdx] + secondDigitLetters[secondIdx] + thirdDigitLetters[thirdIdx] + fourthDigitLetters[fourthIdx];
                                digitLetterComboArr.push(combo);
                            }
                        }
                    }
                }
            }
        }
    }

    return digitLetterComboArr;
};