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

        # Morris Traversal:
        total_sum = 0
        curr_sum = 0
        depth = 0

        current_node = root

        while(current_node is not None):
            if current_node.left is None:
                curr_sum = (curr_sum * 10) + current_node.val

                # Found Leaf Node on the rightSubTree & it doesn't have left child
                if current_node.right is None:
                    total_sum += curr_sum
                
                current_node = current_node.right
            else:
                prev_node = current_node.left
                depth = 1
                while (prev_node.right is not None) and (prev_node.right != current_node):
                    prev_node = prev_node.right
                    depth = depth + 1
                
                if prev_node.right is None:
                    prev_node.right = current_node
                    curr_sum = (curr_sum * 10) + current_node.val
                    current_node = current_node.left
                else:
                    prev_node.right = None
                    # Found Leaf Node on the leftSubTree & it doesn't have right child
                    if prev_node.left is None:
                        total_sum += curr_sum
                        
                    # Backtrack to the root node, and reset the curr_sum
                    curr_sum = curr_sum // (10 ** depth)
                    current_node = current_node.right
            
        return total_sum