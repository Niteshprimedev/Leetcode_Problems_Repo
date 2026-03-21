class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        /*
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
        */

        // Another solution => Clean Code;
        int endRowIdx = x + k;
        int endColIdx = y + k;

        for(int colIdx = y; colIdx < endColIdx; colIdx++){
            int endRow = endRowIdx - 1;
            for(int strtRow = x; strtRow < endRowIdx; strtRow++){
                if(strtRow >= endRow) break;

                int strtRowVal = grid[strtRow][colIdx];
                grid[strtRow][colIdx] = grid[endRow][colIdx];
                grid[endRow][colIdx] = strtRowVal;

                endRow -= 1;
            }
        }

        return grid;
    }
}