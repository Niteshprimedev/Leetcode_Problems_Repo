# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest_row_values_arr = []

        def traverse(current_node, curr_node_depth, largest_row_values_arr):
            # Base case:
            if current_node is None:
                return largest_row_values_arr
            
            if(len(largest_row_values_arr) == curr_node_depth):
                largest_row_values_arr.append(current_node.val)
            else:
                largest_row_values_arr[curr_node_depth] = max(largest_row_values_arr[curr_node_depth], current_node.val)
            traverse(current_node.left, curr_node_depth + 1, largest_row_values_arr)
            traverse(current_node.right, curr_node_depth + 1, largest_row_values_arr)
            
            return largest_row_values_arr
        return traverse(root, 0, largest_row_values_arr)