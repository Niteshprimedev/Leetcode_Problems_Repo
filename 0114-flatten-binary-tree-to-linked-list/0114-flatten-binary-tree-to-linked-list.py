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
        
        '''
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
        '''

        # Solution 1: Stack & Pointers SOLUTION
        current_node = root
        tree_nodes_stack = []

        while current_node:
            if current_node.right:
                tree_nodes_stack.append(current_node.right)
            if current_node.left:
                tree_nodes_stack.append(current_node.left)
            if tree_nodes_stack:
                new_node = tree_nodes_stack.pop()
                current_node.left = None
                current_node.right = new_node

            current_node = current_node.right
        
        return root

        '''
        # Solution 2: Recursive Version:

        if not root:
            return root

        right_nodes_stack = []

        def flatten_pre_dfs_traverse(current_node):
            if current_node and current_node.right:
                right_nodes_stack.append(current_node.right)
            
            if current_node and current_node.left:
                current_node.right = current_node.left
                current_node.left = None

                flatten_pre_dfs_traverse(current_node.right)

            if right_nodes_stack:
                right_node = right_nodes_stack.pop()
                current_node.right = right_node

                flatten_pre_dfs_traverse(current_node.right)

        flatten_pre_dfs_traverse(root)

        return root
        '''       
