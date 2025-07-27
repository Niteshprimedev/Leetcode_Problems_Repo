class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # Logic: count the number of connected nodes in each
        # component and then multiply the number of 
        # connected nodes with other connected nodes to get the pairs
        # 3 components => [4, 1, 2] so the answer would be:
        # 4 * 1 + 4 * 2 + 1 * 2 => 14;

        adjacency_list = {}
        connected_nodes_arr = []
        visited_vertices_map = [False for _ in range(n)]
        total_pairs_count = 0

        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]

            if vertex1 not in adjacency_list:
                adjacency_list[vertex1] = []
            
            if vertex2 not in adjacency_list:
                adjacency_list[vertex2] = []
            
            adjacency_list[vertex1].append(vertex2)
            adjacency_list[vertex2].append(vertex1)
        
        # print(adjacency_list)

        def graphDFSIve(curr_vertex):
            vertices_stack = []

            vertices_stack.append(curr_vertex)
            total_nodes = 0

            while len(vertices_stack) > 0:
                curr_vertex = vertices_stack.pop()

                if not visited_vertices_map[curr_vertex]:
                    total_nodes += 1
                    visited_vertices_map[curr_vertex] = True

                    curr_vertices_neighbors = adjacency_list[curr_vertex]

                    for curr_vertex_neighbor in curr_vertices_neighbors:
                        if not visited_vertices_map[curr_vertex_neighbor]:
                            vertices_stack.append(curr_vertex_neighbor)

            return total_nodes

        for vertex in range(n):
            if vertex in adjacency_list and not visited_vertices_map[vertex]:
                connected_nodes_count = graphDFSIve(vertex)
                connected_nodes_arr.append(connected_nodes_count)
            elif vertex not in adjacency_list:
                connected_nodes_arr.append(1)

        
        '''
        # This below code is a Recipe for TLE;
        for idx_i in range(len(connected_nodes_arr)):
            pairs_count1 = connected_nodes_arr[idx_i]

            for idx_j in range(idx_i + 1, len(connected_nodes_arr)):
                pairs_count2 = connected_nodes_arr[idx_j]
                total_pairs_count += (pairs_count1 * pairs_count2)
        '''

        prefix_sum = 0
        for idx_i in range(len(connected_nodes_arr)):
            pairs_count1 = connected_nodes_arr[idx_i]

            pairs_count2 = n - prefix_sum - pairs_count1
            total_pairs_count += (pairs_count1 * pairs_count2)
            prefix_sum += pairs_count1

        return total_pairs_count

        '''
        # Solution 2: Randomly Picked Problem Solved
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
        for pairs_count1 in connected_comps:
            pairs_count2 = total_connected_sum - connected_count
            curr_unreachable_pairs_count = pairs_count1 * pairs_count2

            total_unreachable_pairs_count += curr_unreachable_pairs_count
            total_connected_sum -= pairs_count1
    
        return total_unreachable_pairs_count
        '''


        

