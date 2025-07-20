# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(current_node1, current_node2):
            if not current_node1 and not current_node2:
                return True
            elif current_node1 and current_node2 and current_node1.val == current_node2.val:
                is_left_subtree = traverse(current_node1.left, current_node2.left)
                is_right_subtree = traverse(current_node1.right, current_node2.right)

                return is_left_subtree and is_right_subtree
            else:
                return False
        
        return traverse(p, q)