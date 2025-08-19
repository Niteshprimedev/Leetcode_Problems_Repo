class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Logic: A better solution than memory => O(N^2)

        n = len(matrix)

        min_heap = []

        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        count_idx = 0
        smallest_val = -1

        while count_idx < k:
            val, r, c = heapq.heappop(min_heap)
            smallest_val = val

            if (c + 1) < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

            count_idx += 1

        return smallest_val

        