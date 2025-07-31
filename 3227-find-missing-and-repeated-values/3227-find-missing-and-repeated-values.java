class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        /*
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
        */

        // Solution 2: USING XOR & Bucketing;
        int gridXOR = 0;

		int mRows = grid.length;
        int nCols = grid[0].length;

        int numVal = 1;

        // Step 1: XOR all grid elements and numbers 1 to n^2
        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                int currVal = grid[rowIdx][colIdx];
                
                gridXOR ^= currVal;
                
                gridXOR ^= numVal;
                numVal += 1;
            }
        }

        // Step 2: Find rightmost set bit
        int bitsPosDiff = ((gridXOR & (gridXOR - 1)) ^ gridXOR);

        int firstNum = 0;
        int secondNum = 0;

        // Step 3: Divide into two groups using bit
        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                int currVal = grid[rowIdx][colIdx];
                
                if((currVal & bitsPosDiff) != 0){
                    firstNum = firstNum ^ currVal;
                }
                else{
                    secondNum = secondNum ^ currVal;
                }
            }
        }

        for(int idx = 1; idx <= (mRows * nCols); idx++){
            if((idx & bitsPosDiff) != 0){
                firstNum = firstNum ^ idx;
            }
            else{
                secondNum = secondNum ^ idx;
            }
        }

        // Step4: Find the repeating;
        int count = 0;
        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                int currVal = grid[rowIdx][colIdx];
                
                if(currVal == firstNum){
                    count++;
                }
            }
        }

        int[] missingAndRepeatingNums = new int[2];
        
        if(count == 2){
            missingAndRepeatingNums[0] = firstNum;
            missingAndRepeatingNums[1] = secondNum;
        }
        else{
            missingAndRepeatingNums[0] = secondNum;
            missingAndRepeatingNums[1] = firstNum;
        }
        
		return missingAndRepeatingNums;
    }
}