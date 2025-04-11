# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        # Post Order Traversal:
        total_sum = 0

        def traverse(current_node, curr_path_sum, total_sum):
            # BASE CASE:
            if not current_node:
                return total_sum
            
            curr_path_sum = (curr_path_sum * 10) + current_node.val
            total_sum = traverse(current_node.left, curr_path_sum, total_sum)
            total_sum = traverse(current_node.right, curr_path_sum, total_sum)

            if current_node.left is None and current_node.right is None:
                total_sum += curr_path_sum
                return total_sum
            
            return total_sum

        total_sum = traverse(root, 0, total_sum)

        return total_sum
        '''
        # Edge case: empty tree
        if not root:
            return 0

        total_sum = 0
        current_node = root

        # Initialize the stack with tuple: (node, current path sum)
        stack = deque([(current_node, 0)])
        # print('stack', stack)

        # Iterative DFS Preorder Traversal
        while(len(stack)):
            current_node, curr_path_sum = stack.pop()
            # Build the number by adding the current digit
            curr_path_sum = (curr_path_sum * 10) + current_node.val

            # If it's a leaf node, add the path sum to total
            if(current_node.left is None and current_node.right is None):
                total_sum += curr_path_sum

            # Push right child first so left gets processed first (preorder style)
            if(current_node.right is not None):
                stack.append((current_node.right, curr_path_sum))

            if(current_node.left is not None):
                stack.append((current_node.left, curr_path_sum))
            
        return total_sum