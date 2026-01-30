class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(lambda: defaultdict(int))
        change_lengths = set(len(sub) for sub in original)
        
        for i, start in enumerate(original):
            end = changed[i]
            c = cost[i]
            
            if end in adj[start]:
                adj[start][end] = min(adj[start][end], c)
            else:
                adj[start][end] = c
        
        
        @cache
        def dijkstra(start, end):
            heap = [(0, start)]
            costs = defaultdict(lambda: inf)
            costs[start] = 0
            while heap:
                path_cost, curr = heapq.heappop(heap)
                if curr == end:
                    return path_cost
                for nei in adj[curr]:
                    nei_cost = adj[curr][nei]
                    
                    new_cost = nei_cost + path_cost
                    
                    if new_cost < costs[nei]:
                        costs[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))
            return inf
        

        @cache
        def dfs(i):
            #let dfs(i) be the cost of matching everything at i and onwards assuming everything before i is matched
            if i >= len(target):
                return 0
           
            c = inf if target[i] != source[i] else dfs(i+1) #if they match save default cost as just continue
            for length in change_lengths:
                t_sub = target[i:i+length]
                s_sub = source[i:i+length]
                trans_cost = dijkstra(s_sub, t_sub)

                if trans_cost != inf:
                    c = min(c, trans_cost + dfs(i+length))
            return c
        
        ans = dfs(0)
        
        
        return ans if ans != inf else -1