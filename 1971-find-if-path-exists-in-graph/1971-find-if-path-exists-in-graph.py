class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Logic: Simple BFS/DFS can do the job
        # start from the source vertex and then 
        # if you ever reach the destination vertex
        # that means path exists else path does not exist;

        adj_list = {}
        visited_vertices_map = {}
        is_path_exist = False

        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]

            if vertex1 not in adj_list:
                adj_list[vertex1] = []

            if vertex2 not in adj_list:
                adj_list[vertex2] = []

            adj_list[vertex1].append(vertex2)
            adj_list[vertex2].append(vertex1)

        def graphDFSIve(curr_vertex):
            vertices_stack = []

            vertices_stack.append(curr_vertex)
            is_path_exist = False

            while len(vertices_stack) > 0:
                curr_vertex = vertices_stack.pop()

                if curr_vertex == destination:
                    is_path_exist = True
                    break

                if curr_vertex not in visited_vertices_map:
                    visited_vertices_map[curr_vertex] = 'visited'
                    curr_vertex_neighbors = adj_list[curr_vertex]

                    for curr_neighbor_vertex in curr_vertex_neighbors:
                        if curr_neighbor_vertex not in visited_vertices_map:
                            vertices_stack.append(curr_neighbor_vertex)
            
            return is_path_exist
        
        is_path_exist = graphDFSIve(source)

        return is_path_exist