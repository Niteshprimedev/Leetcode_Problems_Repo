class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        m_rows = len(grid)
        n_cols = len(grid[0])

        visited_vertices_map = [[False for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_num_of_islands = 0

        def graphDFSIve(curr_pos):
            vertices_stack = []

            vertices_stack.append(curr_pos)

            while len(vertices_stack) > 0:
                row_idx, col_idx = vertices_stack.pop()

                if not visited_vertices_map[row_idx][col_idx]:
                    visited_vertices_map[row_idx][col_idx] = True

                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == "1":
                            if not visited_vertices_map[new_row_idx][new_col_idx]:
                                vertices_stack.append((new_row_idx, new_col_idx))



        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if not visited_vertices_map[row_idx][col_idx] and grid[row_idx][col_idx] == "1":
                    graphDFSIve((row_idx, col_idx))
                    total_num_of_islands += 1
        
        return total_num_of_islands
        '''
        
        '''
        # Solution: Update -> Modified the if condition under loop;
        m_rows = len(grid)
        n_cols = len(grid[0])

        visited_vertices_map = [[False for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_num_of_islands = 0

        def graphDFSIve(curr_pos):
            vertices_stack = []

            vertices_stack.append(curr_pos)

            while len(vertices_stack) > 0:
                row_idx, col_idx = vertices_stack.pop()

                if not visited_vertices_map[row_idx][col_idx]:
                    visited_vertices_map[row_idx][col_idx] = True

                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == "1":
                            # if not visited_vertices_map[new_row_idx][new_col_idx]:
                            vertices_stack.append((new_row_idx, new_col_idx))



        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if not visited_vertices_map[row_idx][col_idx] and grid[row_idx][col_idx] == "1":
                    graphDFSIve((row_idx, col_idx))
                    total_num_of_islands += 1
        
        return total_num_of_islands
        '''
        
        # Solution using Graph BFS Algo
        # Solution: Update -> Modified the if condition under loop;
        m_rows = len(grid)
        n_cols = len(grid[0])

        visited_vertices_map = [[False for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_num_of_islands = 0

        def graphBFSIve(curr_pos):
            vertices_queue = []

            vertices_queue.append(curr_pos)

            while len(vertices_queue) > 0:
                row_idx, col_idx = vertices_queue.pop(0)

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == "1":
                        if not visited_vertices_map[new_row_idx][new_col_idx]:
                            visited_vertices_map[new_row_idx][new_col_idx] = True
                            vertices_queue.append((new_row_idx, new_col_idx))



        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if not visited_vertices_map[row_idx][col_idx] and grid[row_idx][col_idx] == "1":
                    visited_vertices_map[row_idx][col_idx] = True
                    graphBFSIve((row_idx, col_idx))
                    total_num_of_islands += 1
        
        return total_num_of_islands
        