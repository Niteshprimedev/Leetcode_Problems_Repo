class Solution {
    /*
    private int maxCoinsProfit(int rowIdx, int colIdx, int neutralPower, int[][]coins, int[][][] memoDP){
        // Base Case;
        if(rowIdx == coins.length - 1 && colIdx == coins[0].length - 1){
            // System.out.println(coins[rowIdx][colIdx]);
            // if(neutralPower > 0) return 0;
            return coins[rowIdx][colIdx];
        }
        else if(rowIdx == coins.length || colIdx == coins[0].length){
            return Integer.MIN_VALUE;
        }

        // Memoization case;
        if(memoDP[rowIdx][colIdx] != Integer.MIN_VALUE){
            return memoDP[rowIdx][colIdx];
        }

        // Recursive Case;
        int currCellCoin = coins[rowIdx][colIdx];
        int maxProfit = currCellCoin;
        if(currCellCoin < 0 && neutralPower > 0){
            int rightStealCase = maxCoinsProfit(rowIdx, colIdx + 1, neutralPower - 1, coins, memoDP); 
            
            int downStealCase = maxCoinsProfit(rowIdx + 1, colIdx, neutralPower - 1, coins, memoDP);

            maxProfit = Math.max(rightStealCase, downStealCase);
        }

        int rightNotStealCase = currCellCoin + maxCoinsProfit(rowIdx, colIdx + 1, neutralPower, coins, memoDP); 
        int downrightStealCase = currCellCoin + maxCoinsProfit(rowIdx + 1, colIdx, neutralPower, coins, memoDP);

        int currMaxProfit = Math.max(rightNotStealCase, downrightStealCase);

        memoDP[rowIdx][colIdx] = Math.max(maxProfit, currMaxProfit);
        return memoDP[rowIdx][colIdx];
    }

    public int maximumAmount(int[][] coins) {
        int mRows = coins.length;
        int nCols = coins[0].length;

        int[][][] memoDP = new int[mRows][nCols][3];

        for(int[][] currRowCol : memoDP){
            for(int[] currRow : currRowCol){
                Arrays.fill(currRow, Integer.MIN_VALUE);
            }
        }

        return maxCoinsProfit(0, 0, 2, coins, memoDP);
    }
    */

    int NEG = -1_000_000_000;

    private int maxCoinsProfit(int r, int c, int k, int[][] coins, int[][][] dp) {
        int m = coins.length, n = coins[0].length;

        // out of bounds
        if (r >= m || c >= n) return NEG;

        // destination
        if (r == m - 1 && c == n - 1) {
            if (coins[r][c] < 0 && k > 0) return 0;
            return coins[r][c];
        }

        // memo
        if (dp[r][c][k] != Integer.MIN_VALUE) {
            return dp[r][c][k];
        }

        int val = coins[r][c];

        // option 1: take value
        int take = val + Math.max(
            maxCoinsProfit(r, c + 1, k, coins, dp),
            maxCoinsProfit(r + 1, c, k, coins, dp)
        );

        // option 2: neutralize (only if negative)
        int skip = NEG;
        if (val < 0 && k > 0) {
            skip = Math.max(
                maxCoinsProfit(r, c + 1, k - 1, coins, dp),
                maxCoinsProfit(r + 1, c, k - 1, coins, dp)
            );
        }

        return dp[r][c][k] = Math.max(take, skip);
    }

    public int maximumAmount(int[][] coins) {
        int m = coins.length, n = coins[0].length;

        int[][][] dp = new int[m][n][3];

        for (int[][] layer : dp) {
            for (int[] row : layer) {
                Arrays.fill(row, Integer.MIN_VALUE);
            }
        }

        return maxCoinsProfit(0, 0, 2, coins, dp);
    }
}