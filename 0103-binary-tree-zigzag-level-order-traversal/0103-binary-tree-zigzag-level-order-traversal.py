# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        # Logic: BFS Traversal with each alternate level nodes reversed

        zig_zag_level_traversal = []

        if not root:
            return zig_zag_level_traversal

        queue = []
        queue.append(root)
        node_idx = 0
        curr_level = 0

        while(node_idx < len(queue)):   
            curr_level += 1
            level_len = len(queue)

            curr_level_nodes = []

            for idx_i in range(node_idx, level_len):
                current_node = queue[node_idx]

                node_idx += 1

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

                curr_level_nodes.append(current_node.val)
            
            if curr_level % 2 == 0:
                curr_level_nodes = curr_level_nodes[::-1]

            zig_zag_level_traversal.append(curr_level_nodes)
        
        return zig_zag_level_traversal
        '''

        # Logic: BFS Traversal with each alternate level nodes reversed
        def reverse_arr(nodes_arr):
            strt_idx = 0
            end_idx = len(nodes_arr) - 1

            while strt_idx < end_idx:
                nodes_arr[strt_idx], nodes_arr[end_idx] = nodes_arr[end_idx], nodes_arr[strt_idx]

                strt_idx += 1
                end_idx -= 1
            
            return nodes_arr

        zig_zag_level_traversal = []

        if not root:
            return zig_zag_level_traversal

        queue = []
        queue.append(root)
        node_idx = 0
        curr_level = 0

        while(node_idx < len(queue)):   
            curr_level += 1
            level_len = len(queue)

            curr_level_nodes = []

            for idx_i in range(node_idx, level_len):
                current_node = queue[node_idx]

                node_idx += 1

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

                curr_level_nodes.append(current_node.val)
            
            if curr_level % 2 == 0:
                # reverse using two pointers;
                curr_level_nodes = reverse_arr(curr_level_nodes)

            zig_zag_level_traversal.append(curr_level_nodes)
        
        return zig_zag_level_traversal

        '''
        # Logic: BFS Traversal with each alternate level nodes reversed
        # Solution 2: Strategic Traversal from left & right when 
        # we are at odd and even levels in our traversal;

        zig_zag_level_traversal = []

        if not root:
            return zig_zag_level_traversal

        queue = []
        queue.append(root)
        curr_level = 0

        while len(queue) > 0:
            curr_level += 1
            level_len = len(queue)

            curr_level_nodes = []
            curr_level_stack = []

            for idx_i in range(level_len):
                current_node = queue.pop(0)

                if curr_level % 2 == 0:
                    # on even levels push the right & left
                    if current_node.right:
                        curr_level_stack.append(current_node.right)
                    if current_node.left:
                        curr_level_stack.append(current_node.left)
                else:
                    # on odd levels push the left & right
                    if current_node.left:
                        curr_level_stack.append(current_node.left)
                    if current_node.right:
                        curr_level_stack.append(current_node.right)

                curr_level_nodes.append(current_node.val)

            zig_zag_level_traversal.append(curr_level_nodes)

            # for the next level fill the nodes into the queue
            while curr_level_stack:
                queue.append(curr_level_stack.pop())
        
        return zig_zag_level_traversal
        '''