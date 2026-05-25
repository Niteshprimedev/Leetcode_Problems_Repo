# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class PreInBinaryTree():
    def __init__(self):
        self.root = None

    def construct_tree(self, preorder, pre_strt, pre_end, in_strt, in_end, in_hashmap):

        # Base Case:
        if pre_strt > pre_end or in_strt > in_end:
            return None

        node_val = preorder[pre_strt]

        root = TreeNode(node_val)

        in_root = in_hashmap[node_val]
        nodes_count = in_root - in_strt

        left_pre_end = pre_strt + nodes_count

        root.left = self.construct_tree(preorder, pre_strt + 1, left_pre_end, in_strt, in_root - 1, in_hashmap)

        root.right = self.construct_tree(preorder, left_pre_end + 1, pre_end, in_root + 1, in_end, in_hashmap)

        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_els_map = {}

        for idx in range(len(inorder)):
            inorder_els_map[inorder[idx]] = idx
        
        construct_pre_in_bitree = PreInBinaryTree()

        root = construct_pre_in_bitree.construct_tree(preorder, 0, len(preorder) - 1, 0, len(inorder) - 1, inorder_els_map)

        return root
        