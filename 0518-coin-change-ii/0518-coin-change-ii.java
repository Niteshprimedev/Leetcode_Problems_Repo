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
        // add you logic here
		Arrays.sort(coins);
		int totalCoins = coins.length;
		
		int[][] memoDP = new int[totalCoins][amount + 1];
		
		for(int[] currRow : memoDP){
            Arrays.fill(currRow, -1);
        }
		
		return allCoinsCombos(0, coins, amount, memoDP);
    }
}