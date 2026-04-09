class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Solved during DSA Session 12 on June 14
        m_rows = len(isConnected)
        n_cols = len(isConnected[0])

        adjacency_list = {}
        visited_vertices_map = [False] * m_rows

        total_num_of_provinces = 0

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                curr_cell_val = isConnected[row_idx][col_idx]

                if row_idx == col_idx or curr_cell_val == 0:
                    continue
                
                city_vertex1 = row_idx
                city_vertex2 = col_idx

                if city_vertex1 not in adjacency_list:
                    adjacency_list[city_vertex1] = []
                
                adjacency_list[city_vertex1].append(city_vertex2)
        
        # print(adjacency_list)

        def graphDFSIve(curr_city_vertex):
            vertices_stack = []

            vertices_stack.append(curr_city_vertex)

            while len(vertices_stack) > 0:
                curr_city_vertex = vertices_stack.pop()

                if not visited_vertices_map[curr_city_vertex]:
                    visited_vertices_map[curr_city_vertex] = True

                    curr_city_vertices_neighbors = adjacency_list[curr_city_vertex]
                    for curr_city_vertex_neighbor in curr_city_vertices_neighbors:
                        if not visited_vertices_map[curr_city_vertex_neighbor]:          
                            vertices_stack.append(curr_city_vertex_neighbor)
        
        for curr_city_vertex in range(m_rows):
            if curr_city_vertex not in adjacency_list and not visited_vertices_map[curr_city_vertex]:
                total_num_of_provinces += 1
            elif not visited_vertices_map[curr_city_vertex]:
                total_num_of_provinces += 1
                graphDFSIve(curr_city_vertex)
        
        return total_num_of_provinces



