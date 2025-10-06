import java.util.PriorityQueue;
import java.util.Comparator;

class Cell{
    int row;
    int col;
    int time;
    
    public Cell(int row, int col, int time){
        this.row = row;
        this.col = col;
        this.time = time;
    }
}

class Solution {
    public int swimInWater(int[][] grid) {
        // Solution using PriorityQueue;
        int n = grid.length;

        PriorityQueue<Cell> minHeap = new PriorityQueue<>(Comparator.comparingInt(c -> c.time));
        boolean[][] visited = new boolean[n][n];

        for(boolean[] currRow : visited){
            Arrays.fill(currRow, false);
        }

        minHeap.add(new Cell(0, 0, grid[0][0]));
        visited[0][0] = true;

        int minTime = Integer.MAX_VALUE;

        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, 1, 0, -1};

        while(!minHeap.isEmpty()){
            Cell currCell = minHeap.poll();
            int r = currCell.row;
            int c = currCell.col;
            int time = currCell.time;

            if(r == n - 1 && c == n - 1){
                minTime = time;
                break;
            }

            for(int i = 0; i < 4; i++){
                int nr = r + dy[i];
                int nc = c + dx[i];

                if(nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]){
                    visited[nr][nc] = true;
                    minHeap.add(new Cell(nr, nc, Math.max(time, grid[nr][nc])));
                }
            }
        }

        return minTime;
    }
}