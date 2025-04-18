/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    /**
    const numsArrLen = nums.length;
    const memoDP = new Array(numsArrLen).fill(-1).map(() => new Array(numsArrLen + 1).fill(-1));

    function allSubSeqsLen(currIdx, prevElIdx){
        // Base Case:
        if(currIdx === 0){
            return nums[0] < nums[prevElIdx] ? 1 : 0;
        }

        if(memoDP[currIdx][prevElIdx] !== -1){
            return memoDP[currIdx][prevElIdx];
        }

        let pick = 0;


        if(prevElIdx === numsArrLen || nums[currIdx] < nums[prevElIdx]){
            // Pick and Not Pick Case:
            pick = 1 + allSubSeqsLen(currIdx - 1, currIdx);
        }

        // Not Pick Case:
        const notPick = 0 + allSubSeqsLen(currIdx - 1, prevElIdx);

        memoDP[currIdx][prevElIdx] = Math.max(pick, notPick);
        return memoDP[currIdx][prevElIdx];
    }
    return allSubSeqsLen(numsArrLen - 1, numsArrLen);
    */

    // Top Down Approach Without (n + 1) 2D Array memoization:
    // Striver Video: https://www.youtube.com/watch?v=ekcwMsSIzVc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=42&t=269s

    // instead of taking -1 as prev when there is no previous index, 
    // take prev same as index and check with condition (prev == index), 
    // this will not give memory exceed error as you will not need the n+1 2d array, 
    // just n will be enough.

    if(nums.length === 1) return 1;
    
    const numsArrLen = nums.length;
    const memoDP = new Array(numsArrLen).fill(-1).map(() => new Array(numsArrLen).fill(-1));

    function allSubSeqsLen(currIdx, prevElIdx){
        // Base Case:
        if(currIdx === 0){
            return nums[0] < nums[prevElIdx] ? 1 : 0;
        }

        if(memoDP[currIdx][prevElIdx] !== -1){
            return memoDP[currIdx][prevElIdx];
        }

        let pick = 0;
        let notPick = 0;

        if(prevElIdx === currIdx){
            pick = 1 + allSubSeqsLen(currIdx - 1, currIdx);
            notPick = allSubSeqsLen(currIdx - 1, currIdx - 1);
        }else{
            // Pick and Not Pick Case:
            if(nums[currIdx] < nums[prevElIdx]){
                pick = 1 + allSubSeqsLen(currIdx - 1, currIdx);
            }
            // Not Pick Case:
            notPick = allSubSeqsLen(currIdx - 1, prevElIdx);
        }

        memoDP[currIdx][prevElIdx] = Math.max(pick, notPick);
        return memoDP[currIdx][prevElIdx];
    }
    return allSubSeqsLen(numsArrLen - 1, numsArrLen - 1);

    /** 
    // Did not work cause,  memoization was the problem???
    // Did not memoize for prevEl & it goes from -10000 to 10000
    // So we can't store it in array; need to change second variable/state to indices
    const numsArrLen = nums.length;
    const memoDP = new Array(numsArrLen).fill(-1);

    function allSubSeqsLen(currIdx, prevEl){
        // Base Case:
        if(currIdx === 0){
            return nums[0] < prevEl ? 1 : 0;
        }

        if(memoDP[currIdx] !== -1){
            return memoDP[currIdx];
        }

        // let currNum = nums[currIdx];
        // while(currIdx > 1){
        //     if(currNum < prevEl){
        //         const newPrevEl = nums[currIdx];
        //         pick = 1 + allSubSeqsLen(currIdx - 1, prevEl);
        //     }
        // }

        let pick = 0;
        const currEl = nums[currIdx];
        if(currEl < prevEl){
            // Pick and Not Pick Case:
            const newPrevEl = currEl;
            pick = 1 + allSubSeqsLen(currIdx - 1, newPrevEl);

        }
        // Not Pick Case:
        const notPick = 0 + allSubSeqsLen(currIdx - 1, prevEl);

        memoDP[currIdx] = Math.max(pick, notPick);
        return memoDP[currIdx];
    }
    return allSubSeqsLen(numsArrLen - 1, Infinity);
    */

    /** 
    // Did not Work => Just the choices are one here;
    // Brute Force Solution:
    let longestIncSubSeq = 1;

    for(let idxI = 0; idxI < nums.length; idxI++){
        let prevNum = nums[idxI];
        let newLongestIncSubSeq = 1;

        for(let idxJ = idxI + 1; idxJ < nums.length; idxJ++){
            const currNum = nums[idxJ];

            if(currNum > prevNum){
                prevNum = currNum;
                newLongestIncSubSeq += 1;
            }
        }

        longestIncSubSeq = Math.max(longestIncSubSeq, newLongestIncSubSeq);
    }

    return longestIncSubSeq;
    */
};