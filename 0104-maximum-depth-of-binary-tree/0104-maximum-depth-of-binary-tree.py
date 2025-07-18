# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(root):
    if not root:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    left_height = helper(root.left)
    right_height = helper(root.right)
    
    return 1 + max(left_height, right_height)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        # Solution 1: Using DFS
        if root == None:
            return 0
        
        max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return max_depth
        '''
        
        '''
        # Solution 2: Using DFS
        # Solved during DSA Session 11 on June 7

        return helper(root)
        '''

        # Solution 3: Using DFS
        # max_tree_depth = 0

        def traverse(current_node):
            if current_node is None:
                return 0
            left_depth = 1 + traverse(current_node.left)
            right_depth = 1 + traverse(current_node.right)

            return max(left_depth, right_depth)            
        return traverse(root)