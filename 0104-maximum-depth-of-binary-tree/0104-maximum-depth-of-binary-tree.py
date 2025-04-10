# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_tree_depth = 0

        def traverse(current_node):
            if current_node is None:
                return 0
            left_depth = 1 + traverse(current_node.left)
            right_depth = 1 + traverse(current_node.right)

            return max(left_depth, right_depth)            
        return traverse(root)