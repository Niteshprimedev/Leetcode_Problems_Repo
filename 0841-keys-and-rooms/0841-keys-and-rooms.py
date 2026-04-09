class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Logic: Simple, try to visit all the rooms from
        # the room 0 and mark them as visited using BFS or DFS;
        # If all the rooms were visited then we can visit the rooms;
        # else we cannot visit the rooms;

        # Graph Ive DFS solution;
        total_rooms = len(rooms)

        rooms_adj_list = rooms
        visited_rooms_map = {}

        def graphDFS(vertex_key):

            rooms_stack = []
            rooms_stack.append(vertex_key)

            while len(rooms_stack) > 0:
                curr_room_key = rooms_stack.pop()

                if curr_room_key not in visited_rooms_map:
                    visited_rooms_map[curr_room_key] = True
                    neighbors_rooms = rooms_adj_list[curr_room_key]

                    for neighbor_room in reversed(neighbors_rooms):
                        if neighbor_room not in visited_rooms_map:
                            rooms_stack.append(neighbor_room)
        
        graphDFS(0)

        total_visited_rooms = len(visited_rooms_map)

        return total_visited_rooms == total_rooms

        '''
        # Graph Ive BFS Solution:
        total_rooms = len(rooms)

        rooms_adj_list = rooms
        visited_rooms_map = {}

        def graphBFS(curr_room_key):
            rooms_keys_queue = []
            rooms_keys_queue.append(curr_room_key)

            while len(rooms_keys_queue) > 0:
                curr_room_key = rooms_keys_queue.pop(0)

                if curr_room_key not in visited_rooms_map:
                    visited_rooms_map[curr_room_key] = 'visited'

                    neighbors_rooms_keys = rooms_adj_list[curr_room_key]

                    for neighbor_room_key in neighbors_rooms_keys:
                        if neighbor_room_key not in visited_rooms_map:
                            rooms_keys_queue.append(neighbor_room_key)
                            
        graphBFS(0)

        total_visited_rooms = len(visited_rooms_map)
        return total_rooms == total_visited_rooms
        '''