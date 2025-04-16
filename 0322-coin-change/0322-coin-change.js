/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
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
    // Bottom Up Approach:
    if(amount === 0) return 0;

    const totalCoins = coins.length;
    let minNumOfCoins;
    
    // Base Case:
    // The minimum Amount is Infinity;
    const memoDP = new Array(amount + 1).fill(Infinity);
    memoDP[0] = 0; // It takes 0 coins to make 0 amount

    for(let amountIdx = 1; amountIdx <= amount; amountIdx++){

        for(let coin of coins){

            // We can only make a amount using the coins smaller
            // than or equal to my current amount:
            // For amount 3, I can't use coin 5 right? because it will never be possible;
            if(amountIdx - coin >= 0){
                memoDP[amountIdx] = Math.min(memoDP[amountIdx], 1 + memoDP[amountIdx - coin]);
            }
        }
    }

    minNumOfCoins = memoDP[amount];
    return minNumOfCoins === Infinity ? -1 : minNumOfCoins;
};