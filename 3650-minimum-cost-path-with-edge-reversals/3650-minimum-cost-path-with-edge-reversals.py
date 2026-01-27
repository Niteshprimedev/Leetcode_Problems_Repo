class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        # print(graph)

        min_costs = [float('inf') for _ in range(n)]
        visited = set()

        min_heap = []

        heapq.heappush(min_heap, (0, 0))
        min_costs[0] = 0

        while min_heap:
            curr_vertex, weight = heapq.heappop(min_heap)

            if weight > min_costs[curr_vertex]:
                continue
                
            neighbors = graph[curr_vertex]

            for neighbor, nw in neighbors:
                if neighbor not in visited and (weight + nw) < min_costs[neighbor]:
                    min_costs[neighbor] = weight + nw
                    heapq.heappush(min_heap, (neighbor, min_costs[neighbor]))
                    
        return min_costs[n - 1] if min_costs[n - 1] != float('inf') else -1