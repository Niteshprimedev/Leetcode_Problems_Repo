# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = float('-inf')
        max_tree_level = 0

        queue = []
        current_node = root
        curr_level = 0
        current_node_idx = 0

        queue.append(current_node)
        while (len(queue) and current_node_idx < len(queue)):
            level_len = len(queue)
            curr_level += 1

            curr_level_sum = 0

            for idx_i in range(current_node_idx, level_len):
                current_node = queue[current_node_idx]
                current_node_idx += 1

                current_node_val = current_node.val
                curr_level_sum += current_node_val

                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            
            if curr_level_sum > max_level_sum:
                max_tree_level = curr_level
                max_level_sum = curr_level_sum
        
        queue[:] = []
        # print(queue)
        return max_tree_level
