class Pair<R, C>{
    R rowIdx;
    C colIdx;

    Pair(R rowIdx, C colIdx){
        this.rowIdx = rowIdx;
        this.colIdx = colIdx;
    }
}

class Solution {
    void graphBFS(int[] currPos, char[][] grid, boolean[][] visited){
        int mRows = grid.length;
        int nCols = grid[0].length;

        Deque<Pair<Integer, Integer>> queue = new ArrayDeque<>();

        int rowIdx = currPos[0];
        int colIdx = currPos[1];

        queue.addLast(new Pair<>(rowIdx, colIdx));
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        while (queue.size() > 0){
            Pair<Integer, Integer> firstEl = queue.removeFirst();

            rowIdx = firstEl.rowIdx;
            colIdx = firstEl.colIdx;

            for(int idx = 0; idx < 4; idx++){
                int newRowIdx = rowIdx + dx[idx];
                int newColIdx = colIdx + dy[idx];

                if(newRowIdx >= 0 && newRowIdx < mRows && newColIdx >= 0 && newColIdx < nCols && grid[newRowIdx][newColIdx] == '1' && !visited[newRowIdx][newColIdx]){
                    visited[newRowIdx][newColIdx] = true;
                    queue.addLast(new Pair<>(newRowIdx, newColIdx));
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        // DFS Solution;

        int mRows = grid.length;
        int nCols = grid[0].length;
        int totalIslandsCount = 0;

        boolean[][] visited = new boolean[mRows][nCols];

        for(boolean[] currRow : visited){
            Arrays.fill(currRow, false);
        }

        for(int rowIdx = 0; rowIdx < mRows; rowIdx++){
            for(int colIdx = 0; colIdx < nCols; colIdx++){
                if(grid[rowIdx][colIdx] == '1' && !visited[rowIdx][colIdx]){
                    visited[rowIdx][colIdx] = true;
                    graphBFS(new int[]{rowIdx, colIdx}, grid, visited);
                    totalIslandsCount += 1;
                }
            }
        }

        return totalIslandsCount;
    }
}