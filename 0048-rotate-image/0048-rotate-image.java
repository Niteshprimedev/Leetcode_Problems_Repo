class Solution {
    public void rotate(int[][] matrix) {
        int mRows = matrix.length;
		int nCols = matrix[0].length;
		
		for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
			for(int colIdx = rowIdx + 1; colIdx < nCols; colIdx++){
				int cellVal = matrix[rowIdx][colIdx];
				matrix[rowIdx][colIdx] = matrix[colIdx][rowIdx];
				matrix[colIdx][rowIdx] =  cellVal;
			}
		}

		for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
			int endColIdx = nCols - 1;
			for(int strtColIdx = 0; strtColIdx < nCols; strtColIdx++){
				if(strtColIdx >= endColIdx){
					break;
				}
				
				int firstVal = matrix[rowIdx][strtColIdx];
				int lastVal = matrix[rowIdx][endColIdx];

				matrix[rowIdx][strtColIdx] = lastVal;
				matrix[rowIdx][endColIdx] =  firstVal;
				
				endColIdx -= 1;
			}
		}
    }
}