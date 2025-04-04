/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // Top Down Approach;
    if(nums.length < 2){
        return nums[0];
    }

    let maxMoneyRobbery = 0;
    const lastHouseIdx = nums.length - 1;
    const memoDP = new Array(nums.length).fill(-1);

    function chooseOrSkipHouse(houseIdx, houses, memoDP){
        // console.log(houseIdx, (houseIdx < lastHouseIdx) && memoDP[houseIdx]);

        // Base Case;
        if(houseIdx > lastHouseIdx){
            return 0;
        }

        // If the max robbery amount is already computed for the given house
        // then return from the memoDP array;
        if(memoDP[houseIdx] > -1) return memoDP[houseIdx];

        // Else compute the max robbery amount;
        // Return the 
        if(houseIdx === lastHouseIdx){
            const robberyAmount = houses[houseIdx];
            // We need to return the robbery amount for the lastHouseIdx cause
            // we are not making any chooseToRob or skipToRob decision for this house
            // we are directly robbing it only when we did get to this house;
            // Since this is the lastHouse so there's no point in skipping it cause we won't
            // be able to alert the police by robbing the next house so just need to rob this
            return robberyAmount;
        }

        // The decision tree time: chose to rob right subTree;
        const chooseToRob = houses[houseIdx] + chooseOrSkipHouse(houseIdx + 2, houses, memoDP);
        // skip to rob left subTree;
        const skipToRob = chooseOrSkipHouse(houseIdx + 1, houses, memoDP);

        // Calculate the max robbery amount for the current house if
        // when we chose to rob it or when we chose to skip it
        const currMaxRobberyAmount = Math.max(chooseToRob, skipToRob);
        memoDP[houseIdx] = currMaxRobberyAmount;

        // console.log(memoDP[houseIdx], chooseToRob, skipToRob, houseIdx);
        // Return the max robbery amount for the current house
        return memoDP[houseIdx];
    }

    chooseOrSkipHouse(0, nums, memoDP);

    // The robbery amount is greater in the houseIdx = 0
    // so it means the max amount of robbery can be done starting from the house 1
    if(memoDP[0] > memoDP[1]){
        maxMoneyRobbery = memoDP[0];
    }
    // Else if the robbery amount is greater in the houseIdx = 1
    // so it means the max amount of robbery can be done starting from the house 2
    else if(memoDP[0] <= memoDP[1]){
        maxMoneyRobbery = memoDP[1];
    }

    // console.log(memoDP);

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxMoneyRobbery;
};