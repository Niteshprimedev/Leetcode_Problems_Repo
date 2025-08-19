class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int mRows = matrix.length;
        int nCols = matrix[0].length;

        int rowIdx = 0;
        int colIdx = nCols - 1;

        while(rowIdx < mRows && colIdx >= 0){
            if(matrix[rowIdx][colIdx] == target){
                return true;
            }
            else if(matrix[rowIdx][colIdx] > target){
                colIdx -= 1;
            }
            else if(matrix[rowIdx][colIdx] < target){
                rowIdx += 1;
            }
        }

        return false;
    }
}