/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
   
    // Striver's Version: Using Pick and Not Pick Technique:

    let minNumOfCoins = Infinity;
    const totalCoins = coins.length;
    const memoDP = new Array(totalCoins).fill(0).map(() => new Array(amount + 1).fill(-1));

    function allCoinsSumDFS(currIdx, currAmount){
        // Base Case:
        if(currIdx === 0){
            const firstCoin = coins[currIdx];

            const isFirstCoinCanTaken = currAmount % firstCoin === 0 ? true : false;
            if(isFirstCoinCanTaken){
                // how many denominations?
                const coinsDenominations = currAmount / firstCoin;
                return coinsDenominations;
            }
            else{
                return Infinity;
            }
        }

        // If the current coin path is already calculated then return it;
        if(memoDP[currIdx][currAmount] !== -1){
            return memoDP[currIdx][currAmount];
        }

        // Pick Case:
        let pickCurrCoinCounts = Infinity;
        if(coins[currIdx] <= currAmount){
            pickCurrCoinCounts = 1 + allCoinsSumDFS(currIdx, currAmount - coins[currIdx]);
        }

        // Not Pick Case:
        const skipCurrCoinCounts = 0 + allCoinsSumDFS(currIdx - 1, currAmount);

        memoDP[currIdx][currAmount] = Math.min(pickCurrCoinCounts, skipCurrCoinCounts);
        // console.log(memoDP);
        return  memoDP[currIdx][currAmount];
    }
    minNumOfCoins = allCoinsSumDFS(totalCoins - 1, amount);

    return minNumOfCoins === Infinity ? -1 : minNumOfCoins;

        /**
    if(amount === 0) return 0;

    const totalCoins = coins.length;
    let minNumOfCoins;

    function allCoinsSumDFS(currIdx, target){
        // Base Case:
        if(currIdx === 0){
            if (target % coins[currIdx] === 0){
                return target / coins[currIdx];
            }
            return Infinity;
        }

        const notPick = allCoinsSumDFS(currIdx - 1, target);
        let pick = Infinity;

        if(coins[currIdx] <= target){
            pick = 1 + allCoinsSumDFS(currIdx, target - coins[currIdx]);
        }

        return Math.min(pick, notPick);
    }
    minNumOfCoins = allCoinsSumDFS(totalCoins - 1, amount);
    return minNumOfCoins === Infinity ?  -1 : minNumOfCoins;
    */
    
    /**
    // Top Down Approach:
    if(amount === 0) return 0;

    const totalCoins = coins.length;
    let minNumOfCoins;
    const memoDP = new Array(amount + 1).fill(0);

    function allCoinsSumDFS(currAmountSum){
        // Base Case:
        if(currAmountSum === amount){
            return 0;
        }

        if(currAmountSum > amount){
            return Infinity;
        }

        if(memoDP[currAmountSum] !== 0){
            return memoDP[currAmountSum];
        }

        let minCoinsCount = Infinity;

        // dfs(C1) -> dfs(C2), dfs(C4), dfs(C6)
        for(let idxI = 0; idxI < coins.length; idxI++){
            const currCoin = coins[idxI];
            const newCount = 1 + allCoinsSumDFS(currAmountSum + currCoin);
            minCoinsCount = Math.min(minCoinsCount, newCount);
        }

        memoDP[currAmountSum] = minCoinsCount;
        return memoDP[currAmountSum];
    }
    minNumOfCoins = allCoinsSumDFS(0);

    // console.log(memoDP);
    return minNumOfCoins === Infinity ?  -1 : minNumOfCoins;
    
    */

    /** 
    // Bottom Up Approach:
    // Using Striver's Top To Bottom Technique;
    let minNumOfCoins = Infinity;
    const memoDP = new Array(amount + 1).fill(Infinity);

    // Base Case:
    for(let amountIdx = 0; amountIdx <= amount; amountIdx++){
        if(amountIdx === amount){
            memoDP[amountIdx] = 0;
        }
        else{
            memoDP[amountIdx] = Infinity;
        }
    }

    memoDP[0] = 0;
    // console.log(memoDP);

    for(let amountIdx = 1; amountIdx <= amount; amountIdx++){

        let minCoinsCount = Infinity;
        for(let coin of coins){
            let newCount = Infinity;

            if(amountIdx - coin >= 0){
                newCount = 1 + memoDP[amountIdx - coin];
            }
            minCoinsCount = Math.min(minCoinsCount, newCount);
        }

        memoDP[amountIdx] = minCoinsCount;
    }

    // console.log(memoDP);
    minNumOfCoins = memoDP[amount];

    return minNumOfCoins === Infinity ? -1 : minNumOfCoins;

    */
    
    /** 
    // Work in Progresss on April 16th 2025:
    // Space Optimized Bottom Up Approach:
    let minNumOfCoins = Infinity;
    let prevDP = [0];

    // console.log(prevDP);

    for(let amountIdx = 1; amountIdx <= amount; amountIdx++){
        const currDP = new Array(amountIdx _+ 1).fill(Infinity);

        let minCoinsCount = Infinity;

        for(let coin of coins){
            let newCount = Infinity;

            if(amountIdx - coin >= 0){
                newCount = 1 + prevDP[amountIdx - coin];
            }
            minCoinsCount = Math.min(minCoinsCount, newCount);
            currDP[]
        }

        currDP[amountIdx] = minCoinsCount;
        prevDP = currDP;
    }

    // console.log(memoDP);
    minNumOfCoins = prevDP[0];

    return minNumOfCoins === Infinity ? -1 : minNumOfCoins;
    */
};