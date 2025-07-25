# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def pre_order(current_node, max_val):
            # Base Case:
            if not current_node:
                return 0 # no good nodes for null case
            
            current_good_node = 0

            if current_node.val >= max_val:
                current_good_node = 1
            
            max_val = max(current_node.val, max_val)

            left_good_nodes_count = pre_order(current_node.left, max_val)
            right_good_nodes_count = pre_order(current_node.right, max_val)

            return current_good_node + left_good_nodes_count + right_good_nodes_count
        
        return pre_order(root, float('-inf'))