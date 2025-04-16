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
};