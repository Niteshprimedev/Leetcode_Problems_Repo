'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []

        m = len(heights)
        n = len(heights[0])

        top_max = [0] * n

        for r in range(m):
            left_max = 0
            for c in range(n):
                left_max = max(left_max, heights[r][c])

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        # DFS Solution
        def dfs(cell, visited):
            if cell in visited:
                return
            visited.add(cell)
            r, c = cell
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs((nr, nc), visited)

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        for r in range(rows):
            dfs((r, 0), pacific)
            dfs((r, cols - 1), atlantic)
        for c in range(cols):
            dfs((0, c), pacific)
            dfs((rows - 1, c), atlantic)

        return list(pacific & atlantic)
        '''

        '''
        # BFS Solution:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphBFSIve(cell, visited):
            queue = []

            queue.append(cell)
            visited.add(cell)

            while queue:
                r, c = queue.pop(0)

                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]

                    if nr >= 0 and nr < m and nc >= 0 and nc < n and heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) in visited:
                            continue

                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        for r in range(m):
            # pacific water reaching cells reverse:
            # first col
            graphBFSIve((r, 0), pacific)
            
            # atlantic water reaching cells reverse:
            # last col
            graphBFSIve((r, n - 1), atlantic)

        for c in range(n):
            # pacific water reaching cells reverse:
            # top row
            graphBFSIve((0, c), pacific)
            
            # atlantic water reaching cells reverse:
            # bottom row
            graphBFSIve((m - 1, c), atlantic)
        
        return list(pacific & atlantic)
        '''
        
        # BFS Solution: Deque Solution
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def graphBFSIve(cell, visited):
            queue = deque()

            queue.append(cell)
            visited.add(cell)

            while queue:
                r, c = queue.popleft()

                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]

                    if nr >= 0 and nr < m and nc >= 0 and nc < n and heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) in visited:
                            continue

                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        for r in range(m):
            # pacific water reaching cells reverse:
            # first col
            graphBFSIve((r, 0), pacific)
            
            # atlantic water reaching cells reverse:
            # last col
            graphBFSIve((r, n - 1), atlantic)

        for c in range(n):
            # pacific water reaching cells reverse:
            # top row
            graphBFSIve((0, c), pacific)
            
            # atlantic water reaching cells reverse:
            # bottom row
            graphBFSIve((m - 1, c), atlantic)
        
        return list(pacific & atlantic)
