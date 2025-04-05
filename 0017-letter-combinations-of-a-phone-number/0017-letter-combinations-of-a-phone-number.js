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
            // return digitLetterComboArr;
            return [...digitLetterComboArr];
        }

        const digitPhoneLetters = phoneDigiLetterObj[digits[currIdx]];
        let result = digitLetterComboArr;
        digitPhoneLetters.split('').forEach(letter => {
            result = generateCombos(currIdx + 1, currStr + letter, digitLetterComboArr, phoneDigiLetterObj);
        });

        // console.log(result, digitLetterComboArr, 'result');
        return result;
    }
    return generateCombos(0, '', digitLetterComboArr, phoneDigitLettersObj);
    /** 
    // BrainStorming:::
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
    let  firstDigitLetters = phoneDigitLettersObj[firstDigit];
    digitIdx++;

    const isDigitsLenOne = digits.length === 1 ? true : false;

    if(isDigitsLenOne){
        function generateCombos(firstIdx, firstDigiLetters){
            // Base Case;
            if(firstIdx === firstDigitLetters.length){
                return digitLetterComboArr;
            }

            const letterCombo = firstDigiLetters[firstIdx];
            digitLetterComboArr.push(letterCombo);

            return generateCombos(firstIdx + 1, firstDigiLetters);
        }
        return generateCombos(0, firstDigitLetters);
    }

    
    const secondDigit = digits[digitIdx];
    let  secondDigitLetters = phoneDigitLettersObj[secondDigit];
    digitIdx++;

    const isDigitsLenTwo = digits.length === 2 ? true : false;
    if(isDigitsLenTwo){
        function generateCombos(firstIdx, secondIdx, firstDigiLetters, secondDigiLetters){
            // Base Case;
            if(firstIdx === firstDigitLetters.length){
                return digitLetterComboArr;
            }

            if(secondIdx === secondDigiLetters.length){
                return digitLetterComboArr;
            }

            if((firstIdx > 0) && (secondIdx > 0) && firstIdx === secondIdx) return digitLetterComboArr;

            const firstLetter = firstDigiLetters[firstIdx];
            const secondLetter = secondDigiLetters[secondIdx];
            const letterCombo = firstLetter + secondLetter;
            digitLetterComboArr.push(letterCombo);

            console.log(firstIdx, secondIdx);
            generateCombos(firstIdx, secondIdx + 1, firstDigiLetters, secondDigiLetters);

            return generateCombos(firstIdx + 1, 0, firstDigiLetters, secondDigiLetters);
        }
        return generateCombos(0, 0, firstDigitLetters, secondDigitLetters);
    }

    const thirdDigit = digits[digitIdx];
    let  thirdDigitLetters = phoneDigitLettersObj[thirdDigit];
    digitIdx++;

    const isDigitsLenThree = digits.length === 3 ? true : false;
    if(isDigitsLenThree){
        function generateCombos(firstIdx, secondIdx, thirdIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters){
            // Base Case;
            if(firstIdx === firstDigitLetters.length){
                return digitLetterComboArr;
            }
           
            if(secondIdx === secondDigitLetters.length){
                return;
            }

            if(thirdIdx === thirdDigiLetters.length){
                return;
            }

            const firstLetter = firstDigiLetters[firstIdx];
            const secondLetter = secondDigiLetters[secondIdx];
            const thirdLetter = thirdDigiLetters[thirdIdx];
            const letterCombo = firstLetter + secondLetter + thirdLetter;

            digitLetterComboArr.push(letterCombo);

            generateCombos(firstIdx, secondIdx, thirdIdx + 1, firstDigiLetters, secondDigiLetters, thirdDigiLetters);

            generateCombos(firstIdx, secondIdx + 1, thirdIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters);

            return generateCombos(firstIdx + 1, secondIdx, thirdIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters);
        }
        return generateCombos(0, 0, 0, firstDigitLetters, secondDigitLetters, thirdDigitLetters);
    }

    const fourthDigit = digits[digitIdx];
    let  fourthDigitLetters = phoneDigitLettersObj[fourthDigit];

    function generateCombos(firstIdx, secondIdx, thirdIdx, fourthIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters, fourthDigiLetters){
        // Base Cases;
        if(firstIdx === firstDigiLetters.length){
            return 
        }
        if(secondIdx === secondDigitLetters.length){
            return;
        }

        if(thirdIdx === thirdDigiLetters.length){
            return;
        }

        if(fourthIdx === fourthDigiLetters.length){
            return;
        }

        const firstLetter = firstDigiLetters[firstIdx];
        const secondLetter = secondDigiLetters[secondIdx];
        const thirdLetter = thirdDigiLetters[thirdIdx];
        const fourthLetter = fourthDigiLetters[fourthIdx];
        const letterCombo = firstLetter + secondLetter + thirdLetter + fourthLetter;

        digitLetterComboArr.push(letterCombo);

        generateCombos(firstIdx, secondIdx, thirdIdx, fourthIdx + 1, firstDigiLetters, secondDigiLetters, thirdDigiLetters, fourthDigiLetters);

        generateCombos(firstIdx, secondIdx, thirdIdx + 1, fourthIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters, fourthDigiLetters);

        generateCombos(firstIdx, secondIdx + 1, thirdIdx, fourthIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters, fourthDigiLetters);

        return generateCombos(firstIdx + 1, secondIdx, thirdIdx, fourthIdx, firstDigiLetters, secondDigiLetters, thirdDigiLetters, fourthDigiLetters);
    }
    return generateCombos(0, 0, 0, 0, firstDigitLetters, secondDigitLetters, thirdDigitLetters, fourthDigitLetters);


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
    */
};