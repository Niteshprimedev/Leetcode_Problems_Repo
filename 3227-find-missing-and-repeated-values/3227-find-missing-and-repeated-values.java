class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        // add your logic here
		int mRows = grid.length;
        int nCols = grid[0].length;

        int nSquare = (int)Math.pow(nCols, 2);
        int[] nums = new int[nSquare];
        int idx = 0;

        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                int currVal = grid[rowIdx][colIdx];
                
                nums[idx++] = currVal;
            }
        }

        int n = nums.length;

        // System.out.println(n + " " + Arrays.toString(nums));

		int[] missingAndRepeatingNums = new int[2];
		
		int[] numsCopy = new int[n];
		Arrays.fill(numsCopy, -1);
		
		for(int num: nums){
			int numIdx = num - 1;
			
			if(numsCopy[numIdx] == -1){
				numsCopy[numIdx] = num;
			}
			else{
				missingAndRepeatingNums[0] = num;
			}
		}
		
		for(idx = 0; idx < n; idx++){
			int num = numsCopy[idx];
			
			if (num == -1){
				missingAndRepeatingNums[1] = idx + 1;
			}
		}
		
		// System.out.println(Arrays.toString(missingAndRepeatingNums));
			
		return missingAndRepeatingNums;
    }
}