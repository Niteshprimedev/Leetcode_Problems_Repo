class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution using Topo-Sort Algo & inDegree
        # Return the topo_sort_list in reverse order;
        # Kahn's BFS Topo-Sort Algorithm

        topo_sort_list = []
        in_degrees = [0] * numCourses

        adj_list = {}

        for edge in prerequisites:
            vertex1 = edge[0]
            vertex2 = edge[1]

            if vertex1 not in adj_list:
                adj_list[vertex1] = []
            
            in_degrees[vertex2] += 1
            adj_list[vertex1].append(vertex2)
        
        # print(adj_list)

        queue = []

        for idx_i in range(len(in_degrees)):
            degree = in_degrees[idx_i]

            if degree == 0:
                queue.append(idx_i)
        
        while len(queue) > 0:
            curr_vertex = queue.pop(0)
            topo_sort_list.append(curr_vertex)

            if curr_vertex in adj_list:
                for neighbor in adj_list[curr_vertex]:
                    in_degrees[neighbor] -= 1

                    if in_degrees[neighbor] == 0:
                        queue.append(neighbor)

        # print(topo_sort_list)
        if len(topo_sort_list) == numCourses:
            topo_sort_list.reverse()
            return topo_sort_list
        else:
            return []
        
        '''
        # Solution using DFS Topo-Sort Algo 
        # Return the topo_sort_list in reverse order;

        in_degrees = [0] * numCourses
        topo_sort_list = []

        adj_list = {}

        for edge in prerequisites:
            vertex1 = edge[0]
            vertex2 = edge[1]

            if vertex1 not in adj_list:
                adj_list[vertex1] = []
            
            in_degrees[vertex2] += 1
            adj_list[vertex1].append(vertex2)
        
        # print(adj_list)

        stack = []

        for idx_i in range(len(in_degrees)):
            degree = in_degrees[idx_i]

            if degree == 0:
                queue.append(idx_i)
        
        while len(queue) > 0:
            curr_vertex = queue.pop(0)
            topo_sort_list.append(curr_vertex)

            if curr_vertex in adj_list:
                for neighbor in adj_list[curr_vertex]:
                    in_degrees[neighbor] -= 1

                    if in_degrees[neighbor] == 0:
                        queue.append(neighbor)

        # print(topo_sort_list)
        if len(topo_sort_list) == numCourses:
            topo_sort_list.reverse()
            return topo_sort_list
        else:
            return []
        '''