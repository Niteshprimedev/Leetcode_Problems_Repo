# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        '''
        # Post Order Traversal
        def traverse(current_node, curr_path_sum):
            if current_node is None:
                return False
            
            curr_path_sum += current_node.val
            is_left_tree_path_sum = traverse(current_node.left, curr_path_sum)
            is_right_tree_path_sum = traverse(current_node.right, curr_path_sum)

            if current_node.left is None and current_node.right is None:
                if curr_path_sum == targetSum:
                    return True
                else:
                    return False
            
            return is_left_tree_path_sum or is_right_tree_path_sum
        
        return traverse(root, 0)
        '''

        # Morris Traversal:

        current_node = root
        curr_path_sum = 0
        depth = 0

        while(current_node is not None):
            if current_node.left is None:
                curr_path_sum += current_node.val
                # Found Leaf Node: Check right_node is None cause the leftSubtree
                # is already None and this case will mostly be for rightSubTree;
                if (current_node.right is None) and curr_path_sum == targetSum:
                    return True

                current_node = current_node.right

            else:
                prev_node = current_node.left
                depth = prev_node.val
                while (prev_node.right is not None) and prev_node.right != current_node:
                    prev_node = prev_node.right
                    depth += prev_node.val
                
                if prev_node.right is None:
                    prev_node.right = current_node
                    curr_path_sum += current_node.val # Adding the current Path sum
                    current_node = current_node.left

                else:
                    prev_node.right = None
                    # Found Leaf Node: Cause right_node is already None & just check left_node
                    # This case will mostly be true for leftSubTree
                    if (prev_node.left is None) and curr_path_sum == targetSum:
                        return True
                    curr_path_sum -= depth
                    current_node = current_node.right
        

        return False