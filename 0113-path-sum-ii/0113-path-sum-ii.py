# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathsum_equals_target_all_paths = []

        def traverse(current_node, curr_pathsum, curr_pathnodes_arr):
            if not current_node:
                return

            current_node_val = current_node.val
            curr_pathsum += current_node_val

            curr_pathnodes_arr.append(current_node_val)        

            traverse(current_node.left, curr_pathsum, curr_pathnodes_arr.copy())
            traverse(current_node.right, curr_pathsum, curr_pathnodes_arr.copy())

            # leaf node condition
            if current_node.left == None and current_node.right == None:
                is_pathsum_equal = curr_pathsum == targetSum

                if is_pathsum_equal:
                    pathsum_equals_target_all_paths.append(curr_pathnodes_arr)
                    
        traverse(root, 0, [])

        return pathsum_equals_target_all_paths