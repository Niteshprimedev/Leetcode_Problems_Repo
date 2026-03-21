class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        // Use Transpose Technique:
        int endRowIdx = 0;

        for(int colIdx = y; colIdx < (y + k); colIdx++){
            int strtRow = x;
            for(int endRow = (x + k - 1); endRow >= x; endRow--){
                if(endRow <= strtRow) break;

                int strtRowVal = grid[strtRow][colIdx];
                grid[strtRow][colIdx] = grid[endRow][colIdx];
                grid[endRow][colIdx] = strtRowVal;
                
                strtRow += 1;
            }
        }

        return grid;
    }
}