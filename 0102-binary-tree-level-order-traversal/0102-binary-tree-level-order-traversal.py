# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversal = []

        current_node = root

        if(current_node is None):
            return level_order_traversal
            
        queue = []
        node_idx = 0

        queue.append(current_node)

        while(node_idx < len(queue)):
            level_len = len(queue)

            curr_level_nodes = []

            for idx_i in range(node_idx, level_len):
                current_node = queue[node_idx]
                node_idx += 1

                curr_level_nodes.append(current_node.val)

                if(current_node.left):
                    queue.append(current_node.left)
                if(current_node.right):
                    queue.append(current_node.right)
            
            level_order_traversal.append(curr_level_nodes)
        
        return level_order_traversal
