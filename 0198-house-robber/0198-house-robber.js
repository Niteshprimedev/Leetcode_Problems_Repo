/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {

    /**
    // Bottom Up Approach:
    const lastHouseIdx = nums.length;
    const memoDP = new Array(lastHouseIdx).fill(0);
    memoDP[0] = nums[0];

    let maxRobberyAmount = 0;

    for(let currHouseIdx = 1; currHouseIdx < lastHouseIdx; currHouseIdx++){
        // Base Case:
        let choseToRob = nums[currHouseIdx];
        if((currHouseIdx - 2) >= 0){
            choseToRob = nums[currHouseIdx] + memoDP[currHouseIdx - 2];
        }
        const skipToRob = memoDP[currHouseIdx - 1];

        const currMaxRobberyAmount = Math.max(choseToRob, skipToRob);
        memoDP[currHouseIdx] = currMaxRobberyAmount;
    }

    maxRobberyAmount = memoDP[lastHouseIdx - 1];
    return maxRobberyAmount;
    */

    // Top Down Approach;
    let maxMoneyRobbery = 0;
    const lastHouseIdx = nums.length;
    const memoDP = new Array(lastHouseIdx).fill(-1);

    function chooseOrSkipHouseDFS(houseIdx, houses, memoDP){

        // Base Case: if houseIndex goes out of bounds
        if(houseIdx < 0){
            return 0;
        }

        // Return memoDP cached result if already computed
        if(memoDP[houseIdx] !== -1) return memoDP[houseIdx];

        // Choose to rob current house and skip next
        const choseToRob = houses[houseIdx] + chooseOrSkipHouseDFS(houseIdx - 2, houses, memoDP);
        // Or choose to skip current and try next
        const skipToRob = chooseOrSkipHouseDFS(houseIdx - 1, houses, memoDP);

        // Cache the max loot from this house onward
        const currMaxRobberyAmount = Math.max(choseToRob, skipToRob);
        memoDP[houseIdx] = currMaxRobberyAmount;

        // console.log(memoDP[houseIdx], choseToRob, skipToRob, houseIdx);
        // Return the max robbery amount for the current house
        return memoDP[houseIdx];
    }

    // Start the decision tree from the first house
    chooseOrSkipHouseDFS(lastHouseIdx - 1, nums, memoDP);

    console.log(memoDP);
    maxMoneyRobbery = memoDP[lastHouseIdx - 1];

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxMoneyRobbery;
};