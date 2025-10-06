import java.util.ArrayList;
class Solution {
    void dfs(int row, int col, boolean[][] visited, int[][] heights){
        visited[row][col] = true;

        int[][] directions = {
            {0, 1},
            {1, 0}, 
            {0, -1},
            {-1, 0}
        };

        for(int[] d : directions){
            int nr = row + d[0];
            int nc = col + d[1];

            if(nr >= 0 && nr < heights.length && nc >= 0 && nc < heights[0].length && !visited[nr][nc] && heights[nr][nc] >= heights[row][col]){
                dfs(nr, nc, visited, heights);
            }
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;

        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];

        for(int r = 0; r < m; r++){
            // first col;
            dfs(r, 0, pacific, heights);
            
            // last col;
            dfs(r, n - 1, atlantic, heights);
        }

        for(int c = 0; c < n; c++){
            // first row;
            dfs(0, c, pacific, heights);
            dfs(m - 1, c, atlantic, heights);
        }

        List<List<Integer>> result = new ArrayList<>();

        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                if(pacific[r][c] && atlantic[r][c]){
                    result.add(Arrays.asList(r, c));
                }
            }
        }

        return result;
    }
}