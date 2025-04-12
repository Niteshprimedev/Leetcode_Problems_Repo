# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average_nodes_val = []

        current_node = root
        current_node_idx = 0

        queue = []
        queue.append(current_node)

        while(current_node_idx < len(queue)):
            level_len = len(queue)
            curr_level_sum = 0

            nodes_count = 0

            for idx_i in range(current_node_idx, level_len):
                current_node = queue[current_node_idx]
                current_node_idx += 1
                nodes_count += 1

                curr_level_sum += current_node.val
                if(current_node.left):
                    queue.append(current_node.left)
                if(current_node.right):
                    queue.append(current_node.right)
            
            average_sum = (curr_level_sum / nodes_count)
            average_nodes_val.append(average_sum)
        
        return average_nodes_val