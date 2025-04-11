# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # Tricky Morris
        # preorder traverse using Morris, but right before left: root, right, left
        # To make this we will keep tempopary connection with the leftmost leaf from the right part
        # In the end we reverse resulting vector to make the order postorder
        postorder_traversal = []
        if not root:
            return postorder_traversal
        
        current_node = root
        while (current_node is not None):
            if current_node.right is None:
                postorder_traversal.append(current_node.val)
                current_node = current_node.left
            else:
                prev_node = current_node.right
                while (prev_node.left is not None) and (prev_node.left != current_node):
                    prev_node = prev_node.left
                
                if prev_node.left is None:
                    prev_node.left = current_node
                    postorder_traversal.append(current_node.val)
                    current_node = current_node.right
                else:
                    prev_node.left = None
                    current_node = current_node.left
        
        return postorder_traversal[::-1]
        '''

        # Iterative DFS Postorder;
        postorder_traversal = []
        if not root:
            return postorder_traversal

        current_node = root
        stack = []

        stack.append(current_node)

        while (len(stack)):
            current_node = stack.pop()
            postorder_traversal.append(current_node.val)

            if(current_node.left is not None):
                stack.append(current_node.left)
            if(current_node.right is not None):
                stack.append(current_node.right)
        
        return postorder_traversal[::-1]

                
