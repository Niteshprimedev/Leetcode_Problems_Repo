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

    // Optimal Solution:
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

    // console.log(numsElsHashmap, calcGCD(2, 0));

    for(let numIdx = 0; numIdx < nums.length; numIdx++){
        const currNum = nums[numIdx];

        let hashValue = new Map();
        const isCurrNumPresent = numsElsHashmap.has(currNum);
        
        if(isCurrNumPresent){
            hashValue = numsElsHashmap.get(currNum);
            const gcdVal = calcGCD(numIdx, k);
            let idxJ = k / gcdVal;

            // console.log(idxJ, gcdVal);

            for(let [key, value] of hashValue){
                if(key !== numIdx && key % idxJ === 0){
                    countArrPairs += 1;
                }
            }
        }

        hashValue.set(numIdx, currNum);
        numsElsHashmap.set(currNum, hashValue);
    }

    return countArrPairs;
};