class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        '''
        # Logic: Do a BFS Traversal and count the adjacent
        # fresh oranges you can make rotten in each traversal

        m_rows = len(grid)
        n_cols = len(grid[0])

        queue = []
        rotten_oranges_count = 0
        total_minutes_count = [0]

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if grid[row_idx][col_idx] == 2:
                    queue.append((row_idx, col_idx))
                elif grid[row_idx][col_idx] == 1:
                    rotten_oranges_count += 1
        
        if rotten_oranges_count == 0:
            return total_minutes_count[0]
        
        rotten_oranges_count = [rotten_oranges_count]

        visited_cells_map = [[False for _ in range(n_cols)] for _ in range(m_rows)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphBFSIve(queue, total_minutes_count, rotten_oranges_count):
            
            neighbors_queue = []
            unique_neighbors_set = set()

            while len(queue) > 0:
                row_idx, col_idx = queue.pop(0)

                if not visited_cells_map[row_idx][col_idx]:
                    visited_cells_map[row_idx][col_idx] = True
                    
                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 1:
                        fresh_orange_pos = str(new_row_idx) + '-' + str(new_col_idx)
                        if not visited_cells_map[new_row_idx][new_col_idx] and fresh_orange_pos not in unique_neighbors_set:
                            unique_neighbors_set.add(fresh_orange_pos)
                            neighbors_queue.append((new_row_idx, new_col_idx))
            
            print(neighbors_queue)
            if neighbors_queue:
                rotten_oranges_count[0] -= len(neighbors_queue)
                total_minutes_count[0] += 1
                unique_neighbors_set = set()
                graphBFSIve(neighbors_queue, total_minutes_count, rotten_oranges_count)


        graphBFSIve(queue, total_minutes_count, rotten_oranges_count)

        if rotten_oranges_count[0] > 0:
            return -1

        return total_minutes_count[0]
        '''

        # Multisource BFS Solution: Solved during DSA Session 12
        # Logic: Do a BFS Traversal and count the adjacent
        # fresh oranges you can make rotten in each traversal

        m_rows = len(grid)
        n_cols = len(grid[0])

        queue = []
        rotten_oranges_count = 0
        total_minutes_count = [0]
        
        rotten_oranges_map = [[0 for _ in range(n_cols)] for _ in range(m_rows)]

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if grid[row_idx][col_idx] == 2:
                    queue.append((row_idx, col_idx, 0))
                    rotten_oranges_map[row_idx][col_idx] = 2
                elif grid[row_idx][col_idx] == 1:
                    rotten_oranges_count += 1
        
        if rotten_oranges_count == 0:
            return total_minutes_count[0]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphBFSIve(queue, total_minutes_count):
            
            total_rotten_oranges = 0

            while len(queue) > 0:
                row_idx, col_idx, total_minutes = queue.pop(0)
                total_minutes_count[0] = max(total_minutes, total_minutes_count[0])

                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]

                    if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and grid[new_row_idx][new_col_idx] == 1:
                        if rotten_oranges_map[new_row_idx][new_col_idx] == 0:
                            rotten_oranges_map[new_row_idx][new_col_idx] = 2
                            queue.append((new_row_idx, new_col_idx, total_minutes + 1))
                            total_rotten_oranges -= 1
            
            return total_rotten_oranges

        rotten_oranges_count += graphBFSIve(queue, total_minutes_count)

        if rotten_oranges_count > 0:
            return -1

        return total_minutes_count[0]
    
        '''
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
        '''


        