/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    /** 
    // Logic: Traverse through the array twice using idxI & idxJ
    // and for each repeated nums at idxI and idxJ
    // increment the minNumOfOps as well as the reset the idxI to 
    // (minNumOfOps * 3) - 1 value cause every time we remove 3 els;

    // Brute Force Solution:
    let minNumOfOpsForDistinctArrEls = 0;

    for(let idxI = 0; idxI < nums.length; idxI++){
        for(let idxJ = idxI + 1; idxJ < nums.length; idxJ++){
            const isElRepeated = nums[idxI] === nums[idxJ];

            if(isElRepeated){
                minNumOfOpsForDistinctArrEls++;
                idxI = moveIdxByThree();
                
                break;
            }
        }
    }

    function moveIdxByThree(){
        let idx = minNumOfOpsForDistinctArrEls * 3;

        return idx - 1;
    }

    return minNumOfOpsForDistinctArrEls;

    T.C: O(N^2) It is N^2 - N so N^2
    S.C: O(1)
    */

    // Logic:
    // Using Math here, so this time the idea is to loop through the
    // end of the array and whenever we find a repeated el, we stop there
    // we calculate the minNumOfOps require to remove all the elements from 
    // the starting idx 0 so we add 3 if currIdx % 3 = 0, 2 if currIdx % 3 = 1
    // and 1 if currIdx % 3 = 2. And our answer will be currIdx + whatever value
    // we need to add after modulo divided by 3;
    
    const arrLen = nums.length;

    const numsElsHashmap = new Map();
    let minNumOfOpsForDistinctArrEls = 0;

    for(let currIdxI = arrLen - 1; currIdxI >= 0; currIdxI--){
        const currNum = nums[currIdxI];

        const isNumElRepeated = numsElsHashmap.has(currNum);
        if(isNumElRepeated){
            if(currIdxI % 3 === 0){
                minNumOfOpsForDistinctArrEls += (currIdxI + 3) / 3;
            }
            else if(currIdxI % 3 === 1){
                minNumOfOpsForDistinctArrEls += (currIdxI + 2) / 3;
            }
            else if(currIdxI % 3 === 2){
                minNumOfOpsForDistinctArrEls += (currIdxI + 1) / 3;
            }
            break;
        }
        else{
            numsElsHashmap.set(currNum, currIdxI);
        }
    }

    // console.log(numsElsHashmap);
    numsElsHashmap.clear();

    return minNumOfOpsForDistinctArrEls;
};