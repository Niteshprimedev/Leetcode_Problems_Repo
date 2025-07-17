class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        # Observation: BFS gives TLE and DFS Accepted;
        m_rows = len(board)
        n_cols = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphDFSIve(row_idx, col_idx):
            visited = set()

            stack = [(row_idx, col_idx)]

            while len(stack) > 0:
                curr_row_idx, curr_col_idx = stack.pop()
                board[curr_row_idx][curr_col_idx] = -1

                for direction in directions:
                    new_row_idx, new_col_idx = curr_row_idx + direction[0], curr_col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and board[new_row_idx][new_col_idx] == 'O':
                        stack.append((new_row_idx, new_col_idx))

        # Top
        for col_idx in range(n_cols):
            if board[0][col_idx] == 'O':
                graphDFSIve(0, col_idx)

        # Right
        for row_idx in range(m_rows):
            if board[row_idx][n_cols - 1] == 'O':
                graphDFSIve(row_idx, n_cols - 1)

        # Bottom
        for col_idx in range(n_cols):
            if board[m_rows - 1][col_idx] == 'O':
                graphDFSIve(m_rows - 1, col_idx)

        # Left
        for row_idx in range(m_rows):
            if board[row_idx][0] == 'O':
                graphDFSIve(row_idx, 0)
        
        # print(board)
        
        # Surround all the regions now;
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if board[row_idx][col_idx] == 'O':
                    board[row_idx][col_idx] = 'X'
                elif board[row_idx][col_idx] == -1:
                    board[row_idx][col_idx] = 'O'
        
        return board
        '''

        # Solution 1: Capturing the regions that are not
        # connected to boundary first, and then updating 
        # them with 'X' to mark as surrounded;

        # let's do it! so need to modify and capture the Os if
        # it is surrounded by Xs horizontally and vertically;
        # Create a captured regions array and do a dfs traversal
        # to see if the Os cell are connected to the boundary or not;
        # if it is not connected then we can capture all the Os regions;

        m_rows = len(board)
        n_cols = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited_regions_map = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]

        captured_regions = []

        def graphDFSIve(curr_region):
            regions_stack = []

            regions_stack.append(curr_region)

            is_region_edge_not_connected = True

            while len(regions_stack) > 0:
                curr_region = regions_stack.pop()

                row_idx, col_idx = curr_region

                if visited_regions_map[row_idx][col_idx] == -1:
                    visited_regions_map[row_idx][col_idx] = 1

                    if board[row_idx][col_idx] == 'O' and (row_idx == 0 or col_idx == 0 or row_idx == (m_rows - 1) or col_idx == (n_cols - 1)):
                        # print('Hello', row_idx, col_idx)
                        is_region_edge_not_connected = False

                    # curr region's neighbors;
                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        is_valid_pos = new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols
                        if is_valid_pos:
                            if board[new_row_idx][new_col_idx] == 'O' and visited_regions_map[new_row_idx][new_col_idx] == -1:
                                regions_stack.append((new_row_idx, new_col_idx))
            
            return is_region_edge_not_connected

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if board[row_idx][col_idx] == 'O' and visited_regions_map[row_idx][col_idx] == -1:
                    is_region_edge_not_connected = graphDFSIve((row_idx, col_idx))
                    if is_region_edge_not_connected:
                        captured_regions.append((row_idx, col_idx))
        
        # print(captured_regions)

        # Caputre the regions;

        visited_regions_map = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]

        for region in captured_regions:
            regions_stack = []

            regions_stack.append(region)

            while len(regions_stack) > 0:
                curr_region = regions_stack.pop()

                row_idx, col_idx = curr_region

                if visited_regions_map[row_idx][col_idx] == -1:
                    visited_regions_map[row_idx][col_idx] = 1
                    board[row_idx][col_idx] = 'X'

                    # curr region's neighbors;
                    for direction in directions:
                        new_row_idx = row_idx + direction[0]
                        new_col_idx = col_idx + direction[1]

                        is_valid_pos = new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols
                        if is_valid_pos:
                            if board[new_row_idx][new_col_idx] == 'O' and visited_regions_map[new_row_idx][new_col_idx] == -1:
                                regions_stack.append((new_row_idx, new_col_idx))

        '''
        # Solution 2: Similar Solution to Number of Enclaves
        # Same as Striver Version and one of the Comments on the Discussion;

        # Just traverse the matrix once, 
        # and as soon as your enounter a boundary line that has a "O"
        #  in it, run DFS on this "O" and "Save" all the nehgbours of this "O" 
        # from being captured by calling them "S"
        # Now traverse the matrix again and capture all the "O" 
        # that you can inside the matrix except the boundary line

        m_rows = len(board)
        n_cols = len(board[0])

        visited_cells = [[False for _ in range(n_cols)] for _ in range(m_rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphDFSIve(curr_pos):
            stack = [curr_pos]

            while len(stack) > 0:
                row_idx, col_idx = stack.pop()

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and board[new_row_idx][new_col_idx] == 'O' and not visited_cells[new_row_idx][new_col_idx]:
                        visited_cells[new_row_idx][new_col_idx] = True
                        stack.append((new_row_idx, new_col_idx))
            
            return
            


        for col_idx in range(n_cols):
            # Traverse the first row
            if board[0][col_idx] == 'O':
                visited_cells[0][col_idx] = True
                graphDFSIve((0, col_idx))

            # Traverse the last row
            if board[m_rows - 1][col_idx] == 'O':
                visited_cells[m_rows - 1][col_idx] = True
                graphDFSIve((m_rows - 1, col_idx))

        for row_idx in range(m_rows):
            # Traverse the first col
            if board[row_idx][0] == 'O':
                visited_cells[row_idx][0] = True
                graphDFSIve((row_idx, 0))

            # Traverse the last col
            if board[row_idx][n_cols - 1] == 'O':
                visited_cells[row_idx][n_cols - 1] = True
                graphDFSIve((row_idx, n_cols - 1))
        
        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if board[row_idx][col_idx] == 'O' and not visited_cells[row_idx][col_idx]:
                    # print(row_idx, col_idx)
                    # this is the region that is not visited
                    # hence it is now surrounded by 'X'
                    board[row_idx][col_idx] = 'X'
        
        return board
        '''
        

        