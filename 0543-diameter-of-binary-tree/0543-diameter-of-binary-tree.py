# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter_of_binary_tree = [0]

        def traverse(current_node, diameter):
            if current_node is None:
                return 0
            
            left_subtree_height = traverse(current_node.left, diameter)
            right_subtree_height = traverse(current_node.right, diameter)

            diameter[0] = max(diameter[0], left_subtree_height + right_subtree_height)

            return 1 + max(left_subtree_height, right_subtree_height)
        traverse(root, diameter_of_binary_tree)

        return diameter_of_binary_tree[0]