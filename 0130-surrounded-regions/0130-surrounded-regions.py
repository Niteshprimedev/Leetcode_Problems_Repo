class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

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
        

        