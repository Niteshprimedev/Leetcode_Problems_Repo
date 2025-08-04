class Solution {
    /*
    static final int MOD = 1000000007;
	
	private static int allPossiblePaths(int rowIdx, int colIdx, int m, int n, int[][] memoDP){
		// Base Case
		if(rowIdx == m - 1 && colIdx == n - 1){
			return 1;
		}
		else if(rowIdx == m || colIdx == n){
			return 0;
		}
		
		if(memoDP[rowIdx][colIdx] != -1){
			return memoDP[rowIdx][colIdx];
		}
		
		int downPaths = allPossiblePaths(rowIdx + 1, colIdx, m, n, memoDP);
		int rightPaths = allPossiblePaths(rowIdx, colIdx + 1, m, n, memoDP);
		
		memoDP[rowIdx][colIdx] = (int)(((long) downPaths + rightPaths) % MOD);
		
		return memoDP[rowIdx][colIdx];
	}
	
	public int uniquePaths(int m, int n) {
	    // add you logic here
		
		int[][] memoDP = new int[m][n];
		
		for(int rowIdx = 0; rowIdx < m; rowIdx++){
			Arrays.fill(memoDP[rowIdx], -1);
		}
		
		return allPossiblePaths(0, 0, m, n, memoDP);
    }
    */
    
	private static int allPossiblePaths(int rowIdx, int colIdx, int m, int n, int[][] memoDP){
		// Base Case
		if(rowIdx == 0 && colIdx == 0){
			return 1;
		}
		else if(rowIdx < 0 || colIdx < 0){
			return 0;
		}
		
		if(memoDP[rowIdx][colIdx] != -1){
			return memoDP[rowIdx][colIdx];
		}
		
		int downPaths = allPossiblePaths(rowIdx - 1, colIdx, m, n, memoDP);
		int rightPaths = allPossiblePaths(rowIdx, colIdx - 1, m, n, memoDP);
		
		memoDP[rowIdx][colIdx] = downPaths + rightPaths;
		return memoDP[rowIdx][colIdx];
	}
	
	public int uniquePaths(int m, int n) {
	    // add you logic here
		
		int[][] memoDP = new int[m][n];
		
		for(int rowIdx = 0; rowIdx < m; rowIdx++){
			Arrays.fill(memoDP[rowIdx], -1);
		}
		
		return allPossiblePaths(m - 1, n - 1, m, n, memoDP);
    }
}