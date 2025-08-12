# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def traverse(current_node):
            if not current_node:
                return None
            
            left_node = traverse(current_node.left)
            right_node = traverse(current_node.right)

            if left_node and right_node:
                return current_node
            
            if current_node == p or current_node == q:
                return current_node

            return left_node if right_node == None else right_node
        
        current_node = traverse(root)
        return current_node
        