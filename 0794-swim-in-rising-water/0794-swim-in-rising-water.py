class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        n = len(grid)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = [[float('inf') for _ in range(n)] for _ in range(n)]

        min_time = float('inf')
        
        queue = deque()
        queue.append((0, 0, grid[0][0]))
        visited[0][0] = grid[0][0]

        while queue:
            r, c, curr_time = queue.popleft()

            if r == n - 1 and c == n - 1:
                print('hello')
                min_time = min(min_time, curr_time)

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    new_time = max(curr_time, grid[nr][nc])                
                    if new_time < visited[nr][nc]:
                        visited[nr][nc] = new_time
                        queue.append((nr, nc, new_time))
            
        return min_time
        '''

        n = len(grid)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = [[False for _ in range(n)] for _ in range(n)]

        min_time = float('inf')
        
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True

        while min_heap:
            curr_time, r, c = heapq.heappop(min_heap)

            if r == n - 1 and c == n - 1:
                min_time = min(min_time, curr_time)
                break

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if nr >= 0 and nr < n and nc >= 0 and nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(min_heap, (max(grid[nr][nc], curr_time), nr, nc))
            
        return min_time