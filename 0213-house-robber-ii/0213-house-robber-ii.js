/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    /** 
    // Brainstorming & Stuck;
    let maxRobberyAmount = 0;
    const lastHouseIdx = nums.length;
    const memoDP = new Array(lastHouseIdx).fill(-1);

    function robHouses(currHouseIdx, currRobberyAmount, nums, adjHouseIdx){
        // Base Case;
        if(currHouseIdx >= lastHouseIdx){
            return 0;
        }

        // If we already have the robbery amount in our memoDP
        // then return from it;
        if(memoDP[currHouseIdx] > -1) return memoDP[currHouseIdx];

        // Please don't rob the lastHouse if you already robbed the firstHouse
        // cause it will trigger the alert to the police;
        if(currHouseIdx === (lastHouseIdx - 1) && adjHouseIdx === 0){
            return currRobberyAmount;
        }

        if(currHouseIdx === lastHouseIdx) return currRobberyAmount;

        const choseToRobThisHouse = robHouses(currHouseIdx + 2, currRobberyAmount + nums[currHouseIdx], nums, adjHouseIdx);
        if(currHouseIdx === 0){
            adjHouseIdx = -1;
        }
        const skipToRobThisHouse = robHouses(currHouseIdx +  1, currRobberyAmount, nums, adjHouseIdx);

        const currMaxRobberyAmount = Math.max(choseToRobThisHouse, skipToRobThisHouse);

        memoDP[currHouseIdx] = currMaxRobberyAmount;
        // console.log(memoDP);
        return memoDP[currHouseIdx];
    }
    robHouses(0, 0, nums, 0);

    // The robbery amount is greater in the houseIdx = 0
    // so it means the max amount of robbery can be done starting from the house 1
    if(memoDP[0] > memoDP[1]){
        maxRobberyAmount = memoDP[0];
    }
    // Else if the robbery amount is greater in the houseIdx = 1
    // so it means the max amount of robbery can be done starting from the house 2
    else if(memoDP[0] <= memoDP[1]){
        maxRobberyAmount = memoDP[1];
    }

    console.log(memoDP);

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxRobberyAmount;
    */

    let maxRobberyAmount = nums[0];

    let lastHouseIdx = nums.length;

    // Edge case: when there's only one house to rob
    if(lastHouseIdx === 1) return maxRobberyAmount;

    const memoDPWithFirstEl = new Array(lastHouseIdx - 1).fill(-1);
    const memoDPWithLastEl = new Array(lastHouseIdx - 1).fill(-1);

    function robHouses(currHouseIdx, nums, memoDP){
        // console.log(nums);
        // Base Case;
        if(currHouseIdx >= (lastHouseIdx - 1)){
            return 0;
        }

        // If we already have the robbery amount in our memoDP
        // then return from it;
        if(memoDP[currHouseIdx] !== -1) return memoDP[currHouseIdx];

        const choseToRobThisHouse = nums[currHouseIdx] + robHouses(currHouseIdx + 2, nums, memoDP);
        const skipToRobThisHouse = robHouses(currHouseIdx +  1, nums, memoDP);

        const currMaxRobberyAmount = Math.max(choseToRobThisHouse, skipToRobThisHouse);

        memoDP[currHouseIdx] = currMaxRobberyAmount;
        // console.log(memoDP);
        return memoDP[currHouseIdx];
    }
    const maxRobberyAmountWithFirstHouse = robHouses(0, nums.slice(0, lastHouseIdx - 1), memoDPWithFirstEl);
    const maxRobberyAmountWithLastHouse = robHouses(0, nums.slice(1), memoDPWithLastEl);

    // The robbery amount is greater in the houseIdx = 0
    // so it means the max amount of robbery can be done starting from the house 1
    if(maxRobberyAmountWithFirstHouse > maxRobberyAmountWithLastHouse){
        maxRobberyAmount = maxRobberyAmountWithFirstHouse;
    }
    // Else if the robbery amount is greater in the houseIdx = 1
    // so it means the max amount of robbery can be done starting from the house 2
    else if(maxRobberyAmountWithFirstHouse <= maxRobberyAmountWithLastHouse){
        maxRobberyAmount = maxRobberyAmountWithLastHouse;
    }

    console.log(memoDPWithFirstEl, memoDPWithLastEl);
    // console.log(memoDP);

    // Return the maxAmount of Robbery that can be done without alerting the police;
    return maxRobberyAmount;
};