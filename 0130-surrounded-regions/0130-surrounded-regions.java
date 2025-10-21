class Pair{
    int rowIdx;
    int colIdx;

    public Pair(int rowIdx, int colIdx){
        this.rowIdx = rowIdx;
        this.colIdx = colIdx;
    }
}

class Solution {
    private void graphDFSIve(int rowIdx, int colIdx, boolean[][] visitedCells, char[][] board, int[][] directions){
        Stack<Pair> stack = new Stack<>();

        stack.push(new Pair(rowIdx, colIdx));

        while(!stack.isEmpty()){
            Pair currPair = stack.pop();
            rowIdx = currPair.rowIdx;
            colIdx = currPair.colIdx;

            for(int[] direction : directions){
                int newRow = rowIdx + direction[0];
                int newCol = colIdx + direction[1];

                if(newRow >= 0 && newRow < board.length && newCol >= 0 && newCol < board[0].length && board[newRow][newCol] == 'O' && !visitedCells[newRow][newCol]){
                    visitedCells[newRow][newCol] = true;
                    stack.push(new Pair(newRow, newCol));
                }
            }
        }

    }
    public void solve(char[][] board) {
        int mRows = board.length;
        int nCols = board[0].length;

        boolean[][] visitedCells = new boolean[mRows][nCols];

        int[][] directions = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };

        for(boolean[] currRow : visitedCells){
            Arrays.fill(currRow, false);
        }

        for(int colIdx = 0; colIdx < nCols; colIdx++){
            // Traverse the first Row;
            if(board[0][colIdx] == 'O'){
                visitedCells[0][colIdx] = true;
                graphDFSIve(0, colIdx, visitedCells, board, directions);
            }

            // Traverse the last Row;
            if(board[mRows - 1][colIdx] == 'O'){
                visitedCells[mRows - 1][colIdx] = true;
                graphDFSIve(mRows - 1, colIdx, visitedCells, board, directions);
            }
        }

        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            // Traverse the first Col;
            if(board[rowIdx][0] == 'O'){
                visitedCells[rowIdx][0] = true;
                graphDFSIve(rowIdx, 0, visitedCells, board, directions);
            }

            // Traverse the last Col;
            if(board[rowIdx][nCols - 1] == 'O'){
                visitedCells[rowIdx][nCols - 1] = true;
                graphDFSIve(rowIdx, nCols - 1, visitedCells, board, directions);
            }
        }

        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                if(board[rowIdx][colIdx] == 'O' && !visitedCells[rowIdx][colIdx]){
                    board[rowIdx][colIdx] = 'X';
                }
            }
        }
    }
}