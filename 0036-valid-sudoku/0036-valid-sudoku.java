class Solution {
    private boolean isValid(char[] arr){
        /*
        List<Character> charList = new String(arr).chars()
                                    .mapToObj(c -> (char) c)
                                    .filter(c -> c != '.')
                                    .toList();
        Set<Character> charSet = new String(arr).chars()
                                    .mapToObj(c -> (char) c)
                                    .filter(c -> c != '.')
                                    .collect(Collectors.toSet());
        return charList.size() == charSet.size();
        */
        // OR;
        List<Character> charsList = new String(arr).chars()
                                        .mapToObj(c -> (char) c)
                                        .filter(c -> c != '.')
                                        .collect(Collectors.toList());

        return charsList.size() == new HashSet<>(charsList).size();
    }

    private boolean isValidRow(char[][] board){
        for(char[] row : board){
            if(!isValid(row)){
                return false;
            }
        }

        return true;
    }
    private boolean isValidCol(char[][] board){
        int n = board.length;

        for(int c = 0; c < n; c++){
            char[] currCol = new char[9];

            for(int r = 0; r < n; r++){
                currCol[r] = board[r][c];
            }

            if(!isValid(currCol)){
                return false;
            }
        }

        return true;
    }
    private boolean isValidSquare(char[][] board){
        int[] squares = new int[]{0, 3, 6};

        for(int i : squares){
            for(int j : squares){

                char[] currSquare = new char[9];
                int k = 0;

                for(int x = i; x < i + 3; x++){
                    for(int y = j; y < j + 3; y++){
                        currSquare[k++] = board[x][y];
                    }
                }

                if(!isValid(currSquare)){
                    return false;
                }
            }
        }

        return true;
        /*
        int sqVal = 3;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                char[] currSq = new char[9];
                int k = 0;
                for(int x = (i * 3); x < (i * 3 + 3); x++){
                    for(int y = (j * 3); y < (j * 3 + 3); y++){
                        currSq[k++] = board[x][y];
                    }
                }

                if(!isValid(currSq)){
                    return false;
                }
            }
        }

        return true;
        */
    }
    public boolean isValidSudoku(char[][] board) {
        boolean isValidRow = isValidRow(board);
        boolean isValidCol = isValidCol(board);
        boolean isValidSquare = isValidSquare(board);

        return isValidRow && isValidCol && isValidSquare;   
    }
}