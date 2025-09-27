class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m_rows = len(grid)
        n_cols = len(grid[0])

        queue = []

        rotten_oranges = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_fresh_oranges = 0

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if grid[row_idx][col_idx] == 2:
                    queue.append((row_idx, col_idx, 0))
                    rotten_oranges[row_idx][col_idx] = 2
                elif grid[row_idx][col_idx] == 0:
                    rotten_oranges[row_idx][col_idx] = 2
                else:
                    total_fresh_oranges += 1
        
        min_mins_count = 0
        # print(total_fresh_oranges, rotten_oranges)

        while len(queue) > 0:
            # print(queue)
            row_idx, col_idx, curr_time = queue.pop(0)
            min_mins_count = max(min_mins_count, curr_time)
            
            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 1 and rotten_oranges[new_row_idx][new_col_idx] == -1:
                    rotten_oranges[new_row_idx][new_col_idx] = 2
                    queue.append((new_row_idx, new_col_idx, curr_time + 1))
                    total_fresh_oranges -= 1
            
        if total_fresh_oranges == 0:
            return min_mins_count 
        else:
            return -1


        