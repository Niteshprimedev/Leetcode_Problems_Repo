

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {

    /**
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
    */

    // Bottom Up Approach:
    let minStairsClimbingCost = 0;
    const topFloorIdx = cost.length;

    for(let stepIdx = topFloorIdx - 2; stepIdx >= 0; stepIdx--){
        const currCost = cost[stepIdx];
        const stepOneCost = cost[stepIdx + 1];
        const stepTwoCost = (stepIdx + 2) >= topFloorIdx ? 0 : cost[stepIdx + 2];

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
};