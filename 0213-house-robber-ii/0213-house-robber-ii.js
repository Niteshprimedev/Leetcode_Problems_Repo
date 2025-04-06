/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let maxRobberyAmount = nums[0];

    let lastHouseIdx = nums.length;

    // Edge case: when there's only one house to rob
    if(lastHouseIdx === 1) return maxRobberyAmount;

    // Create memoization arrays for two cases: robbing with first house or with last house
    const memoDPWithFirstEl = new Array(lastHouseIdx - 1).fill(-1);
    const memoDPWithLastEl = new Array(lastHouseIdx - 1).fill(-1);

    // Helper function for deciding whether to rob or skip houses
    function chooseOrSkipHouseDFS(currHouseIdx, nums, memoDP){
        // console.log(nums);
        // Base Case: If the current house index exceeds the length, return 0 (no more houses to rob)
        if(currHouseIdx >= (lastHouseIdx - 1)){
            return 0;
        }

        // If the robbery amount has already been computed for the current house, return from memoDP
        if(memoDP[currHouseIdx] !== -1) return memoDP[currHouseIdx];

        // Recursive Case: Choose to rob current house and skip next  
        const choseToRobThisHouse = nums[currHouseIdx] + chooseOrSkipHouseDFS(currHouseIdx + 2, nums, memoDP);
        // Or choose to skip current and try next
        const skipToRobThisHouse = chooseOrSkipHouseDFS(currHouseIdx +  1, nums, memoDP);

        const currMaxRobberyAmount = Math.max(choseToRobThisHouse, skipToRobThisHouse);

        // Store the maximum amount of robbery in the memoDP array
        memoDP[currHouseIdx] = currMaxRobberyAmount;
        // console.log(memoDP);
        return memoDP[currHouseIdx];
    }

    // Calculate max robbery amount by either including the first house or the last house
    const maxRobberyAmountWithFirstHouse = chooseOrSkipHouseDFS(0, nums.slice(0, lastHouseIdx - 1), memoDPWithFirstEl);
    const maxRobberyAmountWithLastHouse = chooseOrSkipHouseDFS(0, nums.slice(1), memoDPWithLastEl);

    // Compare both robbery amounts and return the greater value
    if(maxRobberyAmountWithFirstHouse > maxRobberyAmountWithLastHouse){
        maxRobberyAmount = maxRobberyAmountWithFirstHouse;
    }
    else if(maxRobberyAmountWithFirstHouse <= maxRobberyAmountWithLastHouse){
        maxRobberyAmount = maxRobberyAmountWithLastHouse;
    }

    // console.log(memoDPWithFirstEl, memoDPWithLastEl);

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxRobberyAmount;
};