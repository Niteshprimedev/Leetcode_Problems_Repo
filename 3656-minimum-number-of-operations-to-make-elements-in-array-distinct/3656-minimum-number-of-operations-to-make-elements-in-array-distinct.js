/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
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
};