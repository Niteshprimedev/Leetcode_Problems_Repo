# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return root

        def traverse(current_node):
            new_current_node = current_node

            if current_node:
                right_subtree = current_node.right

                if current_node.left:
                    current_node.right = current_node.left
                    current_node.left = None

                    new_current_node = traverse(current_node.right)

                if right_subtree:
                    new_current_node.right = right_subtree
                    new_current_node = traverse(new_current_node.right)

            return new_current_node
        
        traverse(root)

        return root