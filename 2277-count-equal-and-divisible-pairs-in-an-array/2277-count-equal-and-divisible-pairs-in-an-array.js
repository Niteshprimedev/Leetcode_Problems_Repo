/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    /**
    // Brute Force Solution;
    let countArrPairs = 0;
    for(let idxI = 0; idxI < nums.length; idxI++)  {
        for(let idxJ = idxI + 1; idxJ < nums.length; idxJ++){
            const firstNum = nums[idxI];
            const secondNum = nums[idxJ];

            const areIndicesDivisible = (idxI * idxJ) % k === 0 ? true : false;
            if(firstNum === secondNum && areIndicesDivisible){
                countArrPairs += 1;
            }
        }
    }
    return countArrPairs;

    */

    let countArrPairs = 0;
    function calcGCD(num1, num2){
        while(num2 !== 0){
            let temp = num2;
            num2 = num1 % num2;
            num1 = temp;
        }

        return num1;
    }

    const numsElsHashmap = new Map();

    for(let idxI = 0; idxI < nums.length; idxI++){
        const currNum = nums[idxI];
        const hashKey = currNum;

        let hashValue = new Map();

        const isHashKeyNotPresent = numsElsHashmap.has(hashKey) !== true;
        if(isHashKeyNotPresent){
            numsElsHashmap.set(hashKey, hashValue);
        }

        hashValue = numsElsHashmap.get(hashKey);
        hashValue.set(idxI, hashKey);

        numsElsHashmap.set(hashKey, hashValue);
    }

    // console.log(numsElsHashmap, calcGCD(2, 0));

    // for(let [key, value] of numsElsHashmap){
    //     const indicesHashValuesMap = value;

    //     for(let [idxKey, idxValue] of indicesHashValuesMap){
    //         const gdcVal = calcGCD(idxKey, k);

    //         let idxJ = k / gdcVal;
    //         let tableIdx = 1;

    //         for(idxJ; idxJ < nums.length; idxJ *= tableIdx){

    //             const isValuePresent = idxValue.has(idxJ);
    //             if(isValuePresent && idxJ > idxKey){
    //                 const value = idxValue.get(idxJ);
    //             }  
    //             tableIdx += 1
    //         }
    //     }
    // }

    for(let numIdx = 0; numIdx < nums.length; numIdx++){
        const currNum = nums[numIdx];
        const gcdVal = calcGCD(numIdx, k);

        const hashValue = numsElsHashmap.get(currNum);
        let idxJ = k / gcdVal;

        // console.log(idxJ, gcdVal);

        for(let [key, value] of hashValue){
            if(key !== numIdx && key % idxJ === 0){
                countArrPairs += 1;
            }
        }

        hashValue.delete(numIdx);
        numsElsHashmap.set(currNum, hashValue);

    }

    return countArrPairs;
};