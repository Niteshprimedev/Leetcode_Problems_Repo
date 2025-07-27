class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)
    
        connected_comps = []
        total_connected_sum = 0
        visited = set()

        def graphDFSIve(curr_vertex):
            stack = [curr_vertex]
            total_vertices_count = 1

            while len(stack) > 0:
                curr_vertex = stack.pop()

                for neighbor_v in graph[curr_vertex]:
                    if neighbor_v not in visited:
                        total_vertices_count += 1
                        visited.add(neighbor_v)
                        stack.append(neighbor_v)
            
            return total_vertices_count
    
        for curr_vertex in range(n):
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                total_vertices_count = graphDFSIve(curr_vertex)

                total_connected_sum += total_vertices_count
                connected_comps.append(total_vertices_count)
        
        # print(graph, connected_comps)

        total_unreachable_pairs_count = 0
        for connected_count in connected_comps:
            curr_unreachable_pairs_count = total_connected_sum - connected_count
            curr_unreachable_pairs_count *= connected_count

            total_unreachable_pairs_count += curr_unreachable_pairs_count
            total_connected_sum -= connected_count
    
        return total_unreachable_pairs_count


        

