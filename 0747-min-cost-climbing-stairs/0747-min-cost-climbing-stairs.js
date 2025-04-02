

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {

    /** 
    // Bottom Up Approach:
    let minStairsClimbingCost = 0;
    const topFloorIdx = cost.length;

    for(let stepIdx = topFloorIdx - 2; stepIdx >= 0; stepIdx--){
        const currCost = cost[stepIdx];
        const stepOneCost = cost[stepIdx + 1];
        const stepTwoCost = (stepIdx + 2) === topFloorIdx ? 0 : cost[stepIdx + 2];

        if(stepOneCost < stepTwoCost){
            cost[stepIdx] = currCost + stepOneCost;
        }
        else{
            cost[stepIdx] = currCost + stepTwoCost;
        }
    }

    if(cost[0] < cost[1]){
        minStairsClimbingCost = cost[0];
    }
    else{
        minStairsClimbingCost = cost[1];
    }
    
    return minStairsClimbingCost;
    */

    // Top Down Approach:
    const costArrSize = cost.length;
    const memoDP = new Array(costArrSize).fill(-1);
    const topFloorIdx = cost.length;

    function climbingStairsCost(stairIdx, cost, memoDP){

        if(memoDP[stairIdx] > -1) return memoDP[stairIdx];

        // Base Case;
        if(stairIdx >= topFloorIdx){
            return 0;
        }

        // Step 1;
        const step1StairCost = cost[stairIdx] + climbingStairsCost(stairIdx + 1, cost, memoDP);
        // Step 2;
        const step2StairCost = cost[stairIdx] + climbingStairsCost(stairIdx + 2, cost, memoDP);

        memoDP[stairIdx] = Math.min(step1StairCost, step2StairCost);
        return memoDP[stairIdx];
    }
    climbingStairsCost(0, cost, memoDP);

    minStairsClimbingCost = memoDP[0] < memoDP[1] ? memoDP[0] : memoDP[1];
    return minStairsClimbingCost;

    /** 
    // Solution using DFS;
    // Using Memoization;

    // Tree Traversal DFS & Brute Force Solution;

    let minStairsClimbingCost = Infinity;
    const topFloorIdx = cost.length;

    function climbStairs(stepIdx, currCost){
        // Base Case;
        if(stepIdx === topFloorIdx || stepIdx > topFloorIdx){
            minStairsClimbingCost = Math.min(minStairsClimbingCost, currCost);
            return 0;
        }

        let newCost = currCost;
        if((stepIdx + 1) < topFloorIdx){
            newCost += cost[stepIdx + 1];
        }

        // Take Step 1:
        const step1Cost = climbStairs(stepIdx + 1, newCost);
        
        newCost = currCost;
        if((stepIdx + 2) < topFloorIdx){
            newCost += cost[stepIdx + 2];
        }
        // Take Step 2:
        const step2Cost = climbStairs(stepIdx + 2, newCost);

        return;
    }
    climbStairs(-1, 0);

    return minStairsClimbingCost;
    */

    /** 
    // Brainstorming;;

    while(climbIdx <= cost.length){
        let currIdxCost = cost[climbIdx];
        let nextIdxCost = cost[climbIdx + 1] || 0;

        if(currIdxCost < nextIdxCost){
            minStairsClimbingCost += currIdxCost;
            climbIdx++;
        }
        else {
            minStairsClimbingCost += nextIdxCost;
            climbIdx += 2;
        }
    }

    return minStairsClimbingCost;
    */
};