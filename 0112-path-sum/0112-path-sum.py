# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(current_node, curr_path_sum):
            if current_node is None:
                return False
            
            curr_path_sum += current_node.val
            is_left_tree_path_sum = traverse(current_node.left, curr_path_sum)
            is_right_tree_path_sum = traverse(current_node.right, curr_path_sum)

            if current_node.left is None and current_node.right is None:
                if curr_path_sum == targetSum:
                    return True
                else:
                    return False
            
            return is_left_tree_path_sum or is_right_tree_path_sum
        
        return traverse(root, 0)