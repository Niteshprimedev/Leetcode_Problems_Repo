/**
 * @param {number[]} nums
 * @return {number}
 */


// Easy Brute Force Solution;

var maximumSum = function(nums) {
    const equalSumDigitsHashmap = new Map();
    let isNoTwoNumsWithEqualsDigitsSumFound = true;
    let maxSumWithEqualSumOfDigits = -1;

    for(let num of nums){
        const digitsSumKey = sumOfDigits(num);
        let hashValue = [];

        const isDigitsSumNotAdded = equalSumDigitsHashmap.has(digitsSumKey) !== true;
        if(isDigitsSumNotAdded){
            equalSumDigitsHashmap.set(digitsSumKey, hashValue);
        }

        hashValue = equalSumDigitsHashmap.get(digitsSumKey);
        hashValue.push(num);

        equalSumDigitsHashmap.set(digitsSumKey, hashValue);

        if(hashValue.length >= 2){
            isNoTwoNumsWithEqualsDigitsSumFound = false;
        }
    }

/**
    function sumOfDigits(num){
        const numString = num + '';
        let digitsSum = 0;

        if(numString.length < 2) return num;

        for(let digitChar of numString){
            const digit = Number(digitChar);
            digitsSum += digit;
        }

        return digitsSum;
    }
 */
    function sumOfDigits(num){
        let digitsSum = 0;

        while(num > 0){
            digitsSum += num % 10;
            num = Math.floor(num / 10);
        }
        return digitsSum;
    }

    if(isNoTwoNumsWithEqualsDigitsSumFound){
        return maxSumWithEqualSumOfDigits;
    }

    // console.log(equalSumDigitsHashmap);

    for(let [key, value] of equalSumDigitsHashmap){
        const equalSumDigitsValues = value;
        if(equalSumDigitsValues.length >= 2){
            let maxValue = findMaxValue(equalSumDigitsValues);
            let secondMaxValue = findSecondMaxValue(maxValue, equalSumDigitsValues);
            const newMaxSumWithEqualSumOfDigits = maxValue + secondMaxValue;

            maxSumWithEqualSumOfDigits = Math.max(newMaxSumWithEqualSumOfDigits, maxSumWithEqualSumOfDigits);
        }
    }

    function findMaxValue(numsArr){
        let maxValue = numsArr[0];

        for(let num of numsArr){
            maxValue = Math.max(maxValue, num);
        }

        return maxValue;
    }

    function findSecondMaxValue(maxVal, numsArr){
        let secondMaxValue = -1;

        for(let num of numsArr){
            if(num < maxVal){
                secondMaxValue = Math.max(secondMaxValue, num);
            }
        }

        return secondMaxValue === -1 ? maxVal : secondMaxValue;
    }

    return maxSumWithEqualSumOfDigits;
};


/**
 var maximumSum = function(nums){
    function prerequisite(nums){
        let maxDigitsLength = 0;
        const equalDigitsLengthHashmap = new Map();

        for(let num of nums){
            const hashKey = sumOfDigits(num);
            const hashValue = (equalDigitsLengthHashmap.get(hashKey) || 0) + 1;

            equalDigitsLengthHashmap.set(hashKey, hashValue);
        }

        console.log(equalDigitsLengthHashmap);

        for(let [hashKey, hashValue] of equalDigitsLengthHashmap){
            if(hashValue >= 2){
                maxDigitsLength = Math.max(maxDigitsLength, hashKey);
            }
        }

        return maxDigitsLength;
    }

    const maxDigitsLength = prerequisite(nums);
    console.log(maxDigitsLength);

    function sumOfDigits(num){
        const numString = num + '';
        let digitsSum = 0;

        if(numString.length < 2) return num;

        for(let digitChar of numString){
            const digit = Number(digitChar);
            digitsSum += digit;
        }

        return digitsSum;
    }
    */

    /**
    
    const equalSumDigitsHashmap = new Map();
    let isNoTwoNumsWithEqualsDigitsSumFound = true;
    let maxSumWithEqualSumOfDigits = -1;

    for(let num of nums){
        const numString = num + '';

        if(numString.length === maxDigitsLength){
            const digitsSumKey = sumOfDigits(num);
            let hashValue = [];

            const isDigitsSumNotAdded = equalSumDigitsHashmap.has(digitsSumKey) !== true;
            if(isDigitsSumNotAdded){
                equalSumDigitsHashmap.set(digitsSumKey, hashValue);
            }

            hashValue = equalSumDigitsHashmap.get(digitsSumKey);
            hashValue.push(num);

            equalSumDigitsHashmap.set(digitsSumKey, hashValue);

            if(hashValue.length >= 2){
                isNoTwoNumsWithEqualsDigitsSumFound = false;
            }
        }
    }

    function sumOfDigits(num){
        const numString = num + '';
        let digitsSum = 0;

        if(numString.length < 2) return num;

        for(let digitChar of numString){
            const digit = Number(digitChar);
            digitsSum += digit;
        }

        return digitsSum;
    }

    if(isNoTwoNumsWithEqualsDigitsSumFound){
        return maxSumWithEqualSumOfDigits;
    }

    // console.log(equalSumDigitsHashmap);

    for(let [key, value] of equalSumDigitsHashmap){
        const equalSumDigitsValues = value;
        if(equalSumDigitsValues.length >= 2){
            let maxValue = findMaxValue(equalSumDigitsValues);
            let secondMaxValue = findSecondMaxValue(maxValue, equalSumDigitsValues);
            const newMaxSumWithEqualSumOfDigits = maxValue + secondMaxValue;

            maxSumWithEqualSumOfDigits = Math.max(newMaxSumWithEqualSumOfDigits, maxSumWithEqualSumOfDigits);
        }
    }

    function findMaxValue(numsArr){
        let maxValue = numsArr[0];

        for(let num of numsArr){
            maxValue = Math.max(maxValue, num);
        }

        return maxValue;
    }

    function findSecondMaxValue(maxVal, numsArr){
        let secondMaxValue = -1;

        for(let num of numsArr){
            if(num < maxVal){
                secondMaxValue = Math.max(secondMaxValue, num);
            }
        }

        return secondMaxValue;
    }

    return maxSumWithEqualSumOfDigits;
    
    
 }

 */