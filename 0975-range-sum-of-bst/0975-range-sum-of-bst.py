# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        # Logic: Traverse the BST as long as the node val is not less than low
        # and the high values. And add it to the sum if they satisfy [low, high] range

        bst_range_sum = [0]

        def traverse(current_node):
            if not current_node:
                return

            # if current_node.val < low or current_node.val > high:
            #     return
            
            traverse(current_node.left)
            traverse(current_node.right)

            if current_node.val >= low and current_node.val <= high:
                bst_range_sum[0] += current_node.val
        
        traverse(root)
                
        return bst_range_sum[0]
        '''

        # Logic: Traverse the BST as long as the node val is not less than low
        # and the high values. And add it to the sum if they satisfy [low, high] range

        bst_range_sum = [0]

        def traverse(current_node):
            if not current_node:
                return

            if current_node.val >= low and current_node.val <= high:
                bst_range_sum[0] += current_node.val

            # if it is in range (low, high) then go to both left & right
            if current_node.val > low and current_node.val < high:
                traverse(current_node.left)
                traverse(current_node.right)
            # if it is >= high that means I can't have any valid vals
            # to the right of it, so discard right and go left
            elif current_node.val >= high:
                # print(current_node.val)
                traverse(current_node.left)
            # if it is <= low that means I can't have any valid vals
            # to the left of it, so discard left and go right
            elif current_node.val <= low:
                traverse(current_node.right)
        
        traverse(root)

        return bst_range_sum[0]
        