/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {

    // Top Down Approach;
    let maxMoneyRobbery = 0;
    const lastHouseIdx = nums.length;
    const memoDP = new Array(lastHouseIdx).fill(-1);

    function chooseOrSkipHouseDFS(houseIdx, houses, memoDP){

        // Base Case: if houseIndex goes out of bounds
        if(houseIdx >= lastHouseIdx){
            return 0;
        }

        // Return memoDP cached result if already computed
        if(memoDP[houseIdx] !== -1) return memoDP[houseIdx];

        // Choose to rob current house and skip next
        const choseToRob = houses[houseIdx] + chooseOrSkipHouseDFS(houseIdx + 2, houses, memoDP);
        // Or choose to skip current and try next
        const skipToRob = chooseOrSkipHouseDFS(houseIdx + 1, houses, memoDP);

        // Cache the max loot from this house onward
        const currMaxRobberyAmount = Math.max(choseToRob, skipToRob);
        memoDP[houseIdx] = currMaxRobberyAmount;

        // console.log(memoDP[houseIdx], choseToRob, skipToRob, houseIdx);
        // Return the max robbery amount for the current house
        return memoDP[houseIdx];
    }

    // Start the decision tree from the first house
    chooseOrSkipHouseDFS(0, nums, memoDP);

    // console.log(memoDP);
    maxMoneyRobbery = memoDP[0];

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxMoneyRobbery;
};