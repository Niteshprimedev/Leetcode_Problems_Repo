/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    const memo = new Array(n + 1).fill(0);
    // console.log(memo, n, memo.length);

    function calcClimbSteps(stepIdx, memo){

        // Get the already computed result;
        if(memo[stepIdx] > 0) return memo[stepIdx];

        if(stepIdx > n){
            return 0;
        }
        // Base Case:
        if(stepIdx === n){
            memo[stepIdx] = 1;
            return 1;
        }
        // Step 1;
        const step1Ways = calcClimbSteps(stepIdx + 1, memo);
        // Step 2;
        const step2Ways = calcClimbSteps(stepIdx + 2, memo);

        memo[stepIdx] = step1Ways + step2Ways;
        // console.log(memo);
        return memo[stepIdx];
    }

    return calcClimbSteps(0, memo);

    // return totalDisWays;

    /** 
    // Brute Force Solution:
    let totalDisWays = 0;

    function calcClimbSteps(stepIdx){

        if(stepIdx > n){
            return;
        }
        // Base Case:
        if(stepIdx === n){
            totalDisWays++;
            return;
        }
        // Step 1;
        calcClimbSteps(stepIdx + 1);
        // Step 2;
        calcClimbSteps(stepIdx + 2);
    }

    calcClimbSteps(0);

    return totalDisWays;
    */
};