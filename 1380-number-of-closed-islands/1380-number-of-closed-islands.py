class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        m_rows = len(grid)
        n_cols = len(grid[0])

        total_closed_islands = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        def graphDFSIve(curr_pos):
            stack = [curr_pos]

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 0 and not visited_cells[new_row_idx][new_col_idx]:
                        visited_cells[new_row_idx][new_col_idx] = True
                        stack.append((new_row_idx, new_col_idx))
            
            return

        for col_idx in range(n_cols):
            # Traverse the first row
            if grid[0][col_idx] == 0:
                visited_cells[0][col_idx] = True
                graphDFSIve((0, col_idx))

            # Traverse the last row
            if grid[m_rows - 1][col_idx] == 0:
                visited_cells[m_rows - 1][col_idx] = True
                graphDFSIve((m_rows - 1, col_idx))

        for row_idx in range(m_rows):
            # Traverse the first col
            if grid[row_idx][0] == 0:
                visited_cells[row_idx][0] = True
                graphDFSIve((row_idx, 0))

            # Traverse the last col
            if grid[row_idx][n_cols - 1] == 0:
                visited_cells[row_idx][n_cols - 1] = True
                graphDFSIve((row_idx, n_cols - 1))
        
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if grid[row_idx][col_idx] == 0 and not visited_cells[row_idx][col_idx]:
                    total_closed_islands += 1
                    visited_cells[row_idx][n_cols - 1] = True
                    graphDFSIve((row_idx, col_idx))
        
        return total_closed_islands
        '''

        '''
        # Solution 2: Optimized Traversal when checking closed isLands;
        m_rows = len(grid)
        n_cols = len(grid[0])

        total_closed_islands = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        def graphDFSIve(curr_pos):
            stack = [curr_pos]

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 0 and not visited_cells[new_row_idx][new_col_idx]:
                        visited_cells[new_row_idx][new_col_idx] = True
                        stack.append((new_row_idx, new_col_idx))
            
            return

        for col_idx in range(n_cols):
            # Traverse the first row
            if grid[0][col_idx] == 0:
                visited_cells[0][col_idx] = True
                graphDFSIve((0, col_idx))

            # Traverse the last row
            if grid[m_rows - 1][col_idx] == 0:
                visited_cells[m_rows - 1][col_idx] = True
                graphDFSIve((m_rows - 1, col_idx))

        for row_idx in range(m_rows):
            # Traverse the first col
            if grid[row_idx][0] == 0:
                visited_cells[row_idx][0] = True
                graphDFSIve((row_idx, 0))

            # Traverse the last col
            if grid[row_idx][n_cols - 1] == 0:
                visited_cells[row_idx][n_cols - 1] = True
                graphDFSIve((row_idx, n_cols - 1))
        
        for row_idx in range(1, m_rows - 1):
            for col_idx in range(1, n_cols - 1):
                if grid[row_idx][col_idx] == 0 and not visited_cells[row_idx][col_idx]:
                    total_closed_islands += 1
                    visited_cells[row_idx][n_cols - 1] = True
                    graphDFSIve((row_idx, col_idx))
        
        return total_closed_islands
        '''

        '''
        # Solution 3: Optimized Traversal && Spiral Matrix Traversal;
        m_rows = len(grid)
        n_cols = len(grid[0])

        total_closed_islands = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        def graphDFSIve(curr_pos):
            stack = [curr_pos]

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 0 and not visited_cells[new_row_idx][new_col_idx]:
                        visited_cells[new_row_idx][new_col_idx] = True
                        stack.append((new_row_idx, new_col_idx))
            
            return

        #Top: Traverse the first row
        for col_idx in range(n_cols):
            if grid[0][col_idx] == 0 and not visited_cells[0][col_idx]:
                visited_cells[0][col_idx] = True
                graphDFSIve((0, col_idx))

        #Right: Traverse the last col
        for row_idx in range(m_rows):
            if grid[row_idx][n_cols - 1] == 0 and not visited_cells[row_idx][n_cols - 1]:
                visited_cells[row_idx][n_cols - 1] = True
                graphDFSIve((row_idx, n_cols - 1))

        #Bottom: Traverse the last row
        for col_idx in range(n_cols):
            if grid[m_rows - 1][col_idx] == 0 and not visited_cells[m_rows - 1][col_idx]:
                visited_cells[m_rows - 1][col_idx] = True
                graphDFSIve((m_rows - 1, col_idx))

        # Left: Traverse the first col
        for row_idx in range(m_rows):
            if grid[row_idx][0] == 0 and not visited_cells[row_idx][0]:
                visited_cells[row_idx][0] = True
                graphDFSIve((row_idx, 0))

        # Count number of closed islands now;
        for row_idx in range(1, m_rows - 1):
            for col_idx in range(1, n_cols - 1):
                if grid[row_idx][col_idx] == 0 and not visited_cells[row_idx][col_idx]:
                    total_closed_islands += 1
                    visited_cells[row_idx][n_cols - 1] = True
                    graphDFSIve((row_idx, col_idx))
        
        return total_closed_islands
        '''

        # Solution 4: Discovering open islands and then finding closed islands;
        m_rows = len(grid)
        n_cols = len(grid[0])

        total_closed_islands = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        def graphDFSIve(curr_pos):
            stack = [curr_pos]

            is_island_edge_not_connected = True

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if (row_idx == 0 or col_idx == 0 or row_idx == m_rows - 1 or col_idx == n_cols - 1):
                        is_island_edge_not_connected = False

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 0 and not visited_cells[new_row_idx][new_col_idx]:
                        visited_cells[new_row_idx][new_col_idx] = True
                        stack.append((new_row_idx, new_col_idx))
            
            if is_island_edge_not_connected:
                closed_islands.append((row_idx, col_idx))
            
            return

        closed_islands = []
        
        # Discover open islands first;
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if grid[row_idx][col_idx] == 0 and not visited_cells[row_idx][col_idx]:
                    visited_cells[row_idx][col_idx] = True
                    graphDFSIve((row_idx, col_idx))
        
        # Redundant work: See I am visiting the entire matrix
        # just to find the closed_islands that are connected with edge
        # and then visiting again to 

        # print(closed_islands)
        
        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        # Count the number of closed islands now;
        for closed_island in closed_islands:

            stack = [closed_island]

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                if not visited_cells[row_idx][col_idx]:
                    visited_cells[row_idx][col_idx] = True

                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and not visited_cells[new_row_idx][new_col_idx] and grid[new_row_idx][new_col_idx] == 0:
                            stack.append((new_row_idx, new_col_idx))
            
            total_closed_islands += 1

        
        return total_closed_islands
