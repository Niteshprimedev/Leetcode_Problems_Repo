class Solution {
    private int allDaysBuySellProfits(int priceIdx, int buyFlag, int[] prices, int[][] memoDP){
        // Base Case:
        if(priceIdx == prices.length){
            return 0;
        }

        // Memo Case:
        if(memoDP[priceIdx][buyFlag] != -1){
            return memoDP[priceIdx][buyFlag];
        }

        int maxProfit = 0;
        
        if(buyFlag == 1){
            int chooseToBuy = -prices[priceIdx] + allDaysBuySellProfits(priceIdx + 1, 0, prices, memoDP);
            int skipToBuy = allDaysBuySellProfits(priceIdx + 1, buyFlag, prices, memoDP);
            maxProfit = Math.max(chooseToBuy, skipToBuy);
        }
        else{
            int chooseToSell = prices[priceIdx] + allDaysBuySellProfits(priceIdx + 1, 1, prices, memoDP);
            int skipToSell = allDaysBuySellProfits(priceIdx + 1, buyFlag, prices, memoDP);

            maxProfit = Math.max(chooseToSell, skipToSell);
        }

        memoDP[priceIdx][buyFlag] = maxProfit;
        return memoDP[priceIdx][buyFlag];
    }

    public int maxProfit(int[] prices) {
        // Solution 1: Peek & Valley;
        int n = prices.length;
        int maxProfit = 0;

        int priceIdx = 0;

        while (priceIdx < n){
            int buyPrice = prices[priceIdx++];

            while (priceIdx < n && buyPrice >= prices[priceIdx]){
                buyPrice = prices[priceIdx];
                priceIdx += 1;
            }

            if(priceIdx == n){
                break;
            }

            int sellPrice = prices[priceIdx++];
            
            while(priceIdx < n && sellPrice <= prices[priceIdx]){
                sellPrice = prices[priceIdx];
                priceIdx += 1;
            }

            maxProfit += sellPrice - buyPrice;
        }

        return maxProfit;

        /*
        // SOlution 2: Top Down Approach:
        int totalDays = prices.length;

        int[][] memoDP = new int[totalDays][2];

        for(int[] currRow : memoDP){
            Arrays.fill(currRow, -1);
        }

        allDaysBuySellProfits(0, 1, prices, memoDP);

        return memoDP[0][1];
        */
        
        /*
        // SOlution 3: Bottom Up Approach:
        int totalDays = prices.length;

        int[][] memoDP = new int[totalDays + 1][2];

        for(int[] currRow : memoDP){
            Arrays.fill(currRow, -1);
        }

        // Base Case:
        for(int buyFlag = 0; buyFlag < 2; buyFlag++){
            memoDP[totalDays][buyFlag] = 0;
        }

        for(int priceIdx = totalDays - 1; priceIdx >= 0; priceIdx--){
            for(int buyFlag = 0; buyFlag < 2; buyFlag++){
                int maxProfit = 0;
                
                if(buyFlag == 1){
                    int chooseToBuy = -prices[priceIdx] + memoDP[priceIdx + 1][0];
                    int skipToBuy = memoDP[priceIdx + 1][buyFlag];
                    maxProfit = Math.max(chooseToBuy, skipToBuy);
                }
                else{
                    int chooseToSell = prices[priceIdx] + memoDP[priceIdx + 1][1];
                    int skipToSell = memoDP[priceIdx + 1][buyFlag];

                    maxProfit = Math.max(chooseToSell, skipToSell);
                }

                memoDP[priceIdx][buyFlag] = maxProfit;
            }
        }

        return memoDP[0][1];
        */

        /*
        // SOlution 3: Bottom Up Space Optimized Approach:
        int totalDays = prices.length;

        int[] prevDP = new int[2];

        Arrays.fill(prevDP, -1);

        // Base Case:
        for(int buyFlag = 0; buyFlag < 2; buyFlag++){
            prevDP[buyFlag] = 0;
        }

        for(int priceIdx = totalDays - 1; priceIdx >= 0; priceIdx--){
            int[] currDP = new int[2];
            Arrays.fill(currDP, -1);

            for(int buyFlag = 0; buyFlag < 2; buyFlag++){
                int maxProfit = 0;
                
                if(buyFlag == 1){
                    int chooseToBuy = -prices[priceIdx] + prevDP[0];
                    int skipToBuy = prevDP[buyFlag];
                    maxProfit = Math.max(chooseToBuy, skipToBuy);
                }
                else{
                    int chooseToSell = prices[priceIdx] + prevDP[1];
                    int skipToSell = prevDP[buyFlag];

                    maxProfit = Math.max(chooseToSell, skipToSell);
                }

                currDP[buyFlag] = maxProfit;
            }

            prevDP = currDP;
        }

        return prevDP[1];
        */
    }
}