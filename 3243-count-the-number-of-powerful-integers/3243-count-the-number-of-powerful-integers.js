/**
 * @param {number} start
 * @param {number} finish
 * @param {number} limit
 * @param {string} s
 * @return {number}
 */
var numberOfPowerfulInt = function(start, finish, limit, s) {

    // Source: https://leetcode.com/problems/count-the-number-of-powerful-integers/solutions/6634808/naruto-video-step-by-step-simple-explanation
    let powerfulIntegersCount = 0;

    function count(digits){
        const chakra = digits.toString();
        const prefixLen = chakra.length - s.length;

        if(prefixLen < 0) return 0;

        const memoDP = new Array(prefixLen + 1).fill(0).map(() => [0, 0]);
        // console.log(memoDP);
        
        memoDP[prefixLen][0] = 1
        memoDP[prefixLen][1] = Number(chakra.slice(prefixLen)) >= Number(s) ? 1 : 0;

        for(let idxI = prefixLen - 1; idxI >= 0; idxI--){
            const digit = Number(chakra[idxI]);

            memoDP[idxI][0] = (limit + 1) * memoDP[idxI + 1][0];

            if (digit <= limit){
                memoDP[idxI][1] = (digit * memoDP[idxI + 1][0]) + memoDP[idxI + 1][1];
            }
            else{
                memoDP[idxI][1] = (limit + 1) * memoDP[idxI + 1][0];
            }
        }

        return memoDP[0][1];
    }
    powerfulIntegersCount = count(finish) - count(start - 1);

    return powerfulIntegersCount;
    /** 
    // Break It Down:
    // Brute Force Solution:
    // Generate all possible int between range [start, finish]
    // Check each digit is less than or equal to limit or not
    // Check if the generated digit has s as its suffix or not
    let powerfulIntegersCount = 0;

    for(let numRange = start; numRange <= finish; numRange++){

        if(numRange < Number(s)){
            continue;
        }

        const isDigitIncludesSuffix = digitHasSuffix(numRange);
        const isDigitWithinLimits = isDigitWithinLimit(numRange);

        if(isDigitWithinLimits && isDigitIncludesSuffix){
            powerfulIntegersCount += 1;
        }
    }

    function digitHasSuffix(digit){
        const digitStr = digit.toString();
        
        const strtIdx = digitStr.length - s.length;
        const suffixStr = digitStr.slice(strtIdx);

        return suffixStr === s;
    }

    function isDigitWithinLimit(digit){
        while(digit > 0){
            const digitVal = digit % 10;
            
            // console.log(digit, digitVal);
            digit = Math.floor(digit / 10);

            if(digitVal > limit){
                return false;
            }
        }

        return true;
    }

    // isDigitWithinLimit(20);

    return powerfulIntegersCount;

    */

    /**
    // Trying Optimization but no clueeeee
    // Brute Force Solution
    // Break It Down:
    // Generate all possible int between range [start, finish]
    // Check each digit is less than or equal to limit or not
    // Check if the generated digit has s as its suffix or not
    let powerfulIntegersCount = 0;
    const numS = Number(s);

    const digitsArr = [0,1,2,3,4,5,6,7,8,9];
    let digitIdx = 1;

    let powerfulNumVal;

    if(start <= numS){
        powerfulNumVal = numS;
    }
    else{
        powerfulNumVal = Number(digitsArr[digitIdx] + s);
        digitIdx += 1;
    }

    while(powerfulNumVal <= finish){

        const isDigitIncludesSuffix = digitHasSuffix(powerfulNumVal);
        const isDigitWithinLimits = isDigitWithinLimit(powerfulNumVal);

        if(isDigitWithinLimits && isDigitIncludesSuffix){
            powerfulIntegersCount += 1;
        }

        if(digitIdx >= 1){
            
        }
        else{

        }

        powerfulNumVal = Number(digitsArr[digitIdx] + s);
        digitIdx += 1;
    }

    function digitHasSuffix(digit){
        const digitStr = digit.toString();
        
        const strtIdx = digitStr.length - s.length;
        const suffixStr = digitStr.slice(strtIdx);

        return suffixStr === s;
    }

    function isDigitWithinLimit(digit){
        while(digit > 0){
            const digitVal = digit % 10;
            
            // console.log(digit, digitVal);
            digit = Math.floor(digit / 10);

            if(digitVal > limit){
                return false;
            }
        }

        return true;
    }

    // isDigitWithinLimit(20);

    return powerfulIntegersCount;
    */
};