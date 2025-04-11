/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countSymmetricIntegers = function(low, high) {

    let symmetricNumsCount = 0;

    for(let idxI = low; idxI <= high; idxI++){
        if(idxI < 11 && high >= 11){
            idxI = 11;
        }
        else if(idxI > 99 && idxI < 1001 && high >= 1001){
            idxI = 1001;
        }

        const numVal = idxI;

        const isSymmetric = checkSymmetricNumVal(numVal);
        if(isSymmetric){
            symmetricNumsCount += 1;
        }
    }

    function checkSymmetricNumVal(num){
        const numStr = num.toString();
        const numStrLen = numStr.length;

        if(numStrLen % 2 !== 0) return false;

        const firstDigitIdx = numStrLen / 2;
        const secondDigitIdx = numStrLen / 2;

        const firstDigitStr = numStr.slice(0, firstDigitIdx);
        const secondDigitStr = numStr.slice(firstDigitIdx);

        const firstDigit = digitsSum(firstDigitStr);
        const secondDigit = digitsSum(secondDigitStr);

        if(firstDigit === secondDigit) return true;
        return false;
    }

    function digitsSum(digits){
        let sum = 0;

        for(let digit of digits){
            sum += Number(digit);
        }

        return sum;
    }

    return symmetricNumsCount;

    /** 
    // Brute Force Solution;
    let symmetricNumsCount = 0;

    for(let idxI = low; idxI <= high; idxI++){
        const numVal = idxI;

        const isSymmetric = checkSymmetricNumVal(numVal);
        if(isSymmetric){
            symmetricNumsCount += 1;
        }
    }

    function checkSymmetricNumVal(num){
        const numStr = num.toString();
        const numStrLen = numStr.length;

        if(numStrLen % 2 !== 0) return false;

        const firstDigitIdx = numStrLen / 2;
        const secondDigitIdx = numStrLen / 2;

        const firstDigitStr = numStr.slice(0, firstDigitIdx);
        const secondDigitStr = numStr.slice(firstDigitIdx);

        const firstDigit = digitsSum(firstDigitStr);
        const secondDigit = digitsSum(secondDigitStr);

        if(firstDigit === secondDigit) return true;
        return false;
    }

    function digitsSum(digits){
        let sum = 0;

        for(let digit of digits){
            sum += Number(digit);
        }

        return sum;
    }

    return symmetricNumsCount;
    */
};