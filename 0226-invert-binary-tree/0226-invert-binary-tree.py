class Solution:
    def invertTree(self, root):
        current_node = root

        while current_node is not None: # meaning that the tree traversal is not done
            if current_node.left is not None:
                # Find the rightmost node of the left subtree
                prev_node = current_node.left
                while prev_node.left is not None and prev_node.left != current_node:
                    # while prev node is not None and prev node is not the threaded node
                    prev_node = prev_node.left # this means that the prev_node will go to None
            #for the first traversal before the nodes are threaded;
                if prev_node.left is not None:
                    # Remove the thread and swap, thread is already connected if prev_node is not none
                    prev_node.left = None
                    # Swap the nodes now
                    swap_node = current_node.left
                    current_node.left = current_node.right
                    current_node.right = swap_node
                    current_node = current_node.left # Continue to what was originally the right
                else:
                    # Threading, cause the prev_node is None and the thread is yet to be connected
                    prev_node = current_node.left
                    # Find the rightmost in left subtree
                    while prev_node.right is not None:
                        prev_node = prev_node.right
                    prev_node.right = current_node
                    current_node = current_node.left
                
                # No left child; just swap and go left
            else:
                # Swap the nodes now
                swap_node = current_node.left
                current_node.left = current_node.right
                current_node.right = swap_node
                current_node = current_node.left # Continue to what was originally the right
                
        return root