class Solution {
    private int allCoinsCombos(int idx, int[] coins, int target, int[][] memoDP){
        // Base Case:
		if(target == 0){
			return 1;
		}
		else if(idx >= coins.length){
			return 0;
		}
		
		if(memoDP[idx][target] != -1){
			return memoDP[idx][target];
		}
		
		int pickCase = 0;
		if(coins[idx] <= target){
			pickCase = allCoinsCombos(idx, coins, target - coins[idx], memoDP);
		}
		
		int notPickCase = allCoinsCombos(idx + 1, coins, target, memoDP);
		
		memoDP[idx][target] = pickCase + notPickCase;
		return memoDP[idx][target];
	}
	
    public int change(int amount, int[] coins) {
        /*
        // add you logic here
		Arrays.sort(coins);
		int totalCoins = coins.length;
		
		int[][] memoDP = new int[totalCoins][amount + 1];
		
		for(int[] currRow : memoDP){
            Arrays.fill(currRow, -1);
        }
		
		return allCoinsCombos(0, coins, amount, memoDP);
        */

        // Solution 2: Bottom Up Approach:
        Arrays.sort(coins);
		int totalCoins = coins.length;
		
		int[][] memoDP = new int[totalCoins + 1][amount + 1];
		
		for(int[] currRow : memoDP){
            Arrays.fill(currRow, -1);
        }

        // Base Case:
        for(int idx = totalCoins; idx >= 0; idx--){
            for(int amountIdx = 0; amountIdx <= amount; amountIdx++){
                if(amountIdx == 0){
                    memoDP[idx][0] = 1;
                }
                else if(idx >= totalCoins){
                    memoDP[idx][amountIdx] = 0;
                }
            }
        }
		
        for(int idx = totalCoins - 1; idx >= 0; idx--){
            for(int amountIdx = 0; amountIdx <= amount; amountIdx++){
                int pickCase = 0;
                if(coins[idx] <= amountIdx){
                    pickCase = memoDP[idx][amountIdx - coins[idx]];
                }
                
                int notPickCase = memoDP[idx + 1][amountIdx];
                
                memoDP[idx][amountIdx] = pickCase + notPickCase;
            }
        }
		return memoDP[0][amount];
    }
}