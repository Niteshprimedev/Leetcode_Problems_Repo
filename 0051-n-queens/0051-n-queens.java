class Solution {
    /*
    private boolean isValidPosition(int rowIdx, int colIdx, int n, String[][] chessBoard){
        // Check top Rows;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            if(chessBoard[newRow][colIdx] == "Q"){
                return false;
            }
        }

        // Check left Cols;
        for(int newCol = colIdx - 1; newCol >= 0; newCol--){
            if(chessBoard[rowIdx][newCol] == "Q"){
                return false;
            }
        }

        // Check Diagonally;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            // Check top left cells;
            int newCol = colIdx - (rowIdx - newRow);
            if(newCol >= 0 && chessBoard[newRow][newCol] == "Q"){
                return false;
            }

            // Check top right cells;
            newCol = colIdx + (rowIdx - newRow);
            if(newCol < n && chessBoard[newRow][newCol] == "Q"){
                return false;
            }
        }

        return true;
    }

    private List<List<String>> allQueensPos(int rowIdx, int colIdx, int nQueens, int n, String[][] chessBoard){
        List<List<String>> nQueensPlacements = new ArrayList<>();

        // Base Case:
        if(nQueens == 0){
            // all queens placed successfully;
            List<String> placedQueensRows = new ArrayList<>();

            for(int i = 0; i < n; i++){
                String currRow = "";
                for(int j = 0; j < n; j++){
                    currRow += chessBoard[i][j];
                }

                placedQueensRows.add(currRow);
            }

            nQueensPlacements.add(placedQueensRows);
            return nQueensPlacements;
        }
        else if(rowIdx == n || colIdx == n){
            return nQueensPlacements;
        }

        // Try placing queen at current position;
        if(isValidPosition(rowIdx, colIdx, n, chessBoard)){
            // place the queen at current position;
            chessBoard[rowIdx][colIdx] = "Q";
            nQueensPlacements = allQueensPos(rowIdx + 1, 0, nQueens - 1, n, chessBoard);

            // backtrack and revert changes;
            chessBoard[rowIdx][colIdx] = ".";
        }

        // Try next column;
        List<List<String>> placedQueensRows = allQueensPos(rowIdx, colIdx + 1, nQueens, n, chessBoard);

        for(List<String> currRow : placedQueensRows){
            nQueensPlacements.add(currRow);
        }

        return nQueensPlacements;
    }

    public List<List<String>> solveNQueens(int n) {
        String[][] chessBoard = new String[n][n];

        for(String[] currRow : chessBoard){
            Arrays.fill(currRow, ".");
        }

        return allQueensPos(0, 0, n, n, chessBoard);
    }
    */

    /*
    // Meta Prep Time Practice:
    private boolean isValidPosition(int rowIdx, int colIdx, int n, String[][] chessBoard){
        // Check top Rows;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            if(chessBoard[newRow][colIdx] == "Q"){
                return false;
            }
        }

        // Check left Cols;
        for(int newCol = colIdx - 1; newCol >= 0; newCol--){
            if(chessBoard[rowIdx][newCol] == "Q"){
                return false;
            }
        }

        // Check Diagonally;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            // Check top left cells;
            int newCol = colIdx - (rowIdx - newRow);
            if(newCol >= 0 && chessBoard[newRow][newCol] == "Q"){
                return false;
            }

            // Check top right cells;
            newCol = colIdx + (rowIdx - newRow);
            if(newCol < n && chessBoard[newRow][newCol] == "Q"){
                return false;
            }
        }

        return true;
    }

    private List<List<String>> allQueensPos(int rowIdx, int colIdx, int nQueens, int n, String[][] chessBoard){
        List<List<String>> nQueensPlacements = new ArrayList<>();

        // Base Case:
        if(nQueens == 0){
            // all queens placed successfully;
            List<String> placedQueensRows = new ArrayList<>();

            for(int i = 0; i < n; i++){
                String currRow = "";
                for(int j = 0; j < n; j++){
                    currRow += chessBoard[i][j];
                }

                placedQueensRows.add(currRow);
            }

            nQueensPlacements.add(placedQueensRows);
            return nQueensPlacements;
        }
        else if(rowIdx == n || colIdx == n){
            return nQueensPlacements;
        }

        // Try placing queen at current position;
        if(isValidPosition(rowIdx, colIdx, n, chessBoard)){
            // place the queen at current position;
            chessBoard[rowIdx][colIdx] = "Q";
            nQueensPlacements = allQueensPos(rowIdx + 1, 0, nQueens - 1, n, chessBoard);

            // backtrack and revert changes;
            chessBoard[rowIdx][colIdx] = ".";
        }

        // Try next column;
        List<List<String>> placedQueensRows = allQueensPos(rowIdx, colIdx + 1, nQueens, n, chessBoard);

        for(List<String> currRow : placedQueensRows){
            nQueensPlacements.add(currRow);
        }

        nQueensPlacements = allQueensPos(rowIdx, colIdx + 1, nQueens, n, chessBoard);
        return nQueensPlacements;
    }

    public List<List<String>> solveNQueens(int n) {
        String[][] chessBoard = new String[n][n];

        for(String[] currRow : chessBoard){
            Arrays.fill(currRow, ".");
        }

        return allQueensPos(0, 0, n, n, chessBoard);
    }
    */

    private boolean isValidPosition(int rowIdx, int colIdx, int n, String[][] chessBoard){
        // Check top rows;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            if(chessBoard[newRow][colIdx] == "Q"){
                return false;
            }
        }

        // Check left cols;
        for(int newCol = colIdx - 1; newCol >= 0; newCol--){
            if(chessBoard[rowIdx][newCol] == "Q"){
                return false;
            }
        }

        // Check left & right Diagonally;
        for(int newRow = rowIdx - 1; newRow >= 0; newRow--){
            // Check top left diagonal;
            int newCol = colIdx - (rowIdx - newRow);
            if(newCol >= 0 && chessBoard[newRow][newCol] == "Q"){
                return false;
            }
            
            // Check top right diagonal;
            newCol = colIdx + (rowIdx - newRow);
            if(newCol < n && chessBoard[newRow][newCol] == "Q"){
                return false;
            }
        }

        // this is a valid pos where Queens don't attack;
        return true;
    }

    private List<List<String>> allQueensPos(int rowIdx, int colIdx, int nQueens, int n, String[][] chessBoard){
        List<List<String>> nQueensPlacements = new ArrayList<>();

        // Base Case:
        if(nQueens == 0){
            // all Queens placed successfully;
            List<String> placedQueensRows = new ArrayList<>();

            for(int i = 0; i < n; i++){
                String currRow = "";
                for(int j = 0; j < n; j++){
                    currRow += chessBoard[i][j];
                }

                placedQueensRows.add(currRow);
            }

            nQueensPlacements.add(placedQueensRows);
            return nQueensPlacements;
        }
        else if(rowIdx == n || colIdx == n){
            return nQueensPlacements;
        }

        // Try placing Queen at current position;
        if(isValidPosition(rowIdx, colIdx, n, chessBoard)){
            // place the Queen at current position
            chessBoard[rowIdx][colIdx] = "Q";
            nQueensPlacements = allQueensPos(rowIdx + 1, 0, nQueens - 1, n, chessBoard);

            // Backtrack and revert the changes;
            chessBoard[rowIdx][colIdx] = ".";
        }

        // Try next column;
        List<List<String>> placedQueensRows = allQueensPos(rowIdx, colIdx + 1, nQueens, n, chessBoard);

        for(List<String> currRow : placedQueensRows){
            nQueensPlacements.add(currRow);
        }

        return nQueensPlacements;
    }

    // Meta Prep Time Practice:
    public List<List<String>> solveNQueens(int n){
        String[][] chessBoard = new String[n][n];

        for(String[] currRow : chessBoard){
            Arrays.fill(currRow, ".");
        }

        return allQueensPos(0, 0, n, n, chessBoard);
    }
}