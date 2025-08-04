class Solution {
    public void setZeroes(int[][] matrix) {
        int firstCol = matrix[0][0];
		int mRows = matrix.length;
		int nCols = matrix[0].length;
		
		for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
			for(int colIdx = 0; colIdx < nCols; colIdx++){
				if(colIdx == 0 && matrix[rowIdx][0] == 0){
					firstCol = 0;
				}
				else if(matrix[rowIdx][colIdx] == 0){
					matrix[rowIdx][0] = 0;
					matrix[0][colIdx] = 0;
				}
			}
		}
		
		// setting the ith rows and jth cols to 0
		for(int rowIdx = 1; rowIdx < mRows; rowIdx++){
			for(int colIdx = 1; colIdx < nCols; colIdx++){
				if(matrix[rowIdx][0] == 0 || matrix[0][colIdx] == 0){
					matrix[rowIdx][colIdx] = 0;
				}
			}
		}
		
		// setting the first row to 0
		for(int colIdx = 1; colIdx < nCols; colIdx++){
			if(matrix[0][0] == 0){
				matrix[0][colIdx] = 0;
			}
		}
		
		// setting the first col to 0
		for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
			if(firstCol == 0){
				matrix[rowIdx][0] = 0;
			}
		}
    }
}