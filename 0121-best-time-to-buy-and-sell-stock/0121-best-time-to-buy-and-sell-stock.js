/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Note: You need to buy on a single day & sell on a different day;
    // Logic: To maximize the profit, I need to buy att the minimum possible cost
    // and sell at maximum possible cost

    // Why DP & What are subProblems here:
    // To calculate the maximum profit for any day in the entire ith day prices
    // If I have Days as Day 1, Day 2, Day 3, Day 4, Day 5 &
    // And if I know the profits for each of these days: D1 - 10, D2 - 5, D3 - -5, D4 - 2, D5 8
    // So the subproblem is to calculate the profit for each of the day and then
    // calculate the maximum profit out of all these days; So D1 - 10
    // For Day 1, the profit is 10
    // For Day 2, the profit is 5
    // For Day 3, the profit is -5
    // For Day 4, the profit is 2
    // For Day 5, the profit is 8
    // When we know the profits of each of the days i.e each of the subproblems
    // then we can easily figure out which of the day would give us the maximum profit out of 
    // all these days?

    /** 
    // Bottom Up Approach:

    const lastDayPriceIdx = prices.length - 1;
    let maxStockSellPrice = prices[lastDayPriceIdx];  

    let maxStockBuySellProfit = 0;

    for(let priceIdx = lastDayPriceIdx - 1; priceIdx >= 0; priceIdx--){
        const currStockBuyPrice = prices[priceIdx];
        const newMaxStockSellPrice = currStockBuyPrice;

        maxStockSellPrice = Math.max(maxStockSellPrice, newMaxStockSellPrice);
        const newMaxStockBuySellProfit = maxStockSellPrice - currStockBuyPrice;

        maxStockBuySellProfit = Math.max(maxStockBuySellProfit, newMaxStockBuySellProfit);
    }

    return maxStockBuySellProfit;
    */

    // Top Down Approach
    const lastDayPriceIdx = prices.length - 1;

    function buyOrSell(buyPriceIdx, sellPriceIdx, prices, maxProfit){
        // Base Case 
        if(sellPriceIdx > lastDayPriceIdx) return maxProfit;

        const stockBuyPrice = prices[buyPriceIdx];
        const stockSellPrice = prices[sellPriceIdx];

        let noSellProfit = 0;
        let sellProfit = 0;

        // We buy the stock if the price is low
        if(stockBuyPrice >= stockSellPrice){
            noSellProfit = buyOrSell(sellPriceIdx, sellPriceIdx + 1, prices, maxProfit);
        }
        // We sell the stock if the price is high
        else{
            sellProfit = stockSellPrice - stockBuyPrice;
            sellProfit = Math.max(sellProfit, buyOrSell(buyPriceIdx, sellPriceIdx + 1, prices, maxProfit));
        }

        // console.log(buyPriceIdx, sellPriceIdx, noSellProfit, sellProfit, maxProfit);

        maxProfit = Math.max(noSellProfit, sellProfit);
        return maxProfit;
    }
    return buyOrSell(0, 1, prices, 0);
};