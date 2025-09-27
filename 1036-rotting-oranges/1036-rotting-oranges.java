class Pair<R,C,M>{
    R rowIdx;
    C colIdx;
    M minutesCount;

    Pair(R rowIdx, C colIdx, M minutesCount){
        this.rowIdx = rowIdx;
        this.colIdx = colIdx;
        this.minutesCount = minutesCount;
    }

};

class Solution {
    public int orangesRotting(int[][] grid) {
        int mRows = grid.length;
        int nCols = grid[0].length;
        
        int minMinutesCount = 0;
        int totalFreshOranges = 0;
        int totalRottenOranges = 0;

        Deque<Pair<Integer, Integer, Integer>> queue = new ArrayDeque<>();
        int[][] rottenOrangesMap = new int[mRows][nCols];

        // right, bottom, left, and top;
        int[] dx = new int[] {1, 0, -1, 0};
        int[] dy = new int[] {0, 1, 0, -1};

        for(int[] currRow : rottenOrangesMap){
            Arrays.fill(currRow, 2);
        }

        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                if(grid[rowIdx][colIdx] == 1){
                    totalFreshOranges += 1;
                    rottenOrangesMap[rowIdx][colIdx] = 1;
                }
                else if(grid[rowIdx][colIdx] == 2){
                    queue.addLast(new Pair<>(rowIdx, colIdx, 0));
                }
            }
        }

        while(queue.size() > 0){
            Pair<Integer, Integer, Integer> firstEl = queue.removeFirst();

            int rowIdx = firstEl.rowIdx;
            int colIdx = firstEl.colIdx;
            int minutesCount = firstEl.minutesCount;

            minMinutesCount = minutesCount;

            for(int idx = 0; idx < 4; idx++){
                int newRowIdx = rowIdx + dx[idx];
                int newColIdx = colIdx + dy[idx];

                if(newRowIdx >= 0 && newRowIdx < mRows && newColIdx >= 0 && newColIdx < nCols && grid[newRowIdx][newColIdx] == 1 && rottenOrangesMap[newRowIdx][newColIdx] == 1){
                    rottenOrangesMap[newRowIdx][newColIdx] = 2;
                    queue.addLast(new Pair<>(newRowIdx, newColIdx, minutesCount + 1));
                    totalRottenOranges += 1;
                }
            }
        }

        // System.out.println(totalFreshOranges + "" + totalRottenOranges);
        // System.out.println(minMinutesCount);
        /**
        if(totalFreshOranges == 0){
            return 0;
        }
        else if(totalFreshOranges == totalRottenOranges){
            return minMinutesCount;
        }

        return -1;
        */

        if(totalFreshOranges == 0){
            return 0;
        }
        else if(totalFreshOranges > totalRottenOranges){
            return -1;
        }

        return minMinutesCount;
    }
}