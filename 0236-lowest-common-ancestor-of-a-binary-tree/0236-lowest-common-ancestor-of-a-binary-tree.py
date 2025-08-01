# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca_node = None

        # Edge Case:
        if p is None or q is None:
            return lca_node
        
        current_node = root

        p_and_q_nodes_list = [False, False]

        def check_nodes(current_node, nodes_list):
            # Base Case:
            if current_node is None:
                return nodes_list
            
            if current_node == p:
                nodes_list[0] = True
            if current_node == q:
                nodes_list[1] = True

            if nodes_list[0] and nodes_list[1]:
                return nodes_list

            check_nodes(current_node.left, nodes_list)
            check_nodes(current_node.right, nodes_list)

            return nodes_list
        check_nodes(current_node, p_and_q_nodes_list)

        # print(p_and_q_nodes_list)

        is_p_node_present = p_and_q_nodes_list[0]
        is_q_node_present = p_and_q_nodes_list[1]

        # Edge Case:
        if not is_p_node_present or not is_q_node_present:
            return lca_node

        current_node = root
        def traverse(current_node):
            # print(current_node)
            # Base Case:
            if current_node is None:
                return None

            if current_node == p or current_node == q:
                return current_node
            
            left_node = traverse(current_node.left)
            right_node = traverse(current_node.right)

            if left_node and right_node:
                return current_node
        
            return left_node if right_node is None else right_node
            # if(left_node is not None):
            #     return left_node
            # else:
            #     return right_node

        lca_node = traverse(current_node)
        return lca_node
