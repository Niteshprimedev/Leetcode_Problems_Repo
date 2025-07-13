class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Edge Case:
        m_rows = len(heights)
        n_cols = len(heights[0])

        if m_rows == 1 and n_cols == 1:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minimum_efforts_path = [[float('inf') for _ in range(n_cols)] for _ in range(m_rows)]
        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        minimum_efforts_path[0][0] = 0

        pq = []
        import heapq

        heapq.heappush(pq, (0, 0, 0))

        while len(pq) > 0:
            curr_effort, row_idx, col_idx = heapq.heappop(pq)
            visited_cells[row_idx][col_idx] = True

            # get the neighbors;
            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and not visited_cells[new_row_idx][new_col_idx]:
                    max_abs_diff = abs(heights[row_idx][col_idx] - heights[new_row_idx][new_col_idx])
                    max_abs_diff = max(max_abs_diff, minimum_efforts_path[row_idx][col_idx])
                    # Perform relaxation and not needed visited;
                    # cause once I found a minimum efforts path for a new cell
                    # then it will only explore those neighbors whose minimum 
                    # efforts path is greater than this new cell;
                    if max_abs_diff < minimum_efforts_path[new_row_idx][new_col_idx]:
                        minimum_efforts_path[new_row_idx][new_col_idx] = max_abs_diff
                        heapq.heappush(pq, (minimum_efforts_path[new_row_idx][new_col_idx], new_row_idx, new_col_idx))

        # print(minimum_efforts_path)
        return minimum_efforts_path[m_rows - 1][n_cols - 1]
        