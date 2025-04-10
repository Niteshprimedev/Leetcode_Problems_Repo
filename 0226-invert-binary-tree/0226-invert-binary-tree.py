class Solution:
    def invertTree(self, root):
        # Logic:
        # Step1: If the current node has no left child, swap the left and right subtree, move to left
        # I said to left (cause it was originally the right)
        # Step2: If the current node has left child, then before moving to the left child, make a connection
        # And here's the trick, we check the left child is connected to the current_node or not cause
        # once we make the thread connection then our right child which was threaded to the current_node for backtracking
        # is actually has become our left child now
        # If the prev_node is connected to the current_node,
        # then remove the connection, swap the left and right subtrees, and move to left child
        # (originally it was right child) 
        # If the prev_node is not connected to the current_node, then find its rightmost child
        # connect it to the current_node and then move to the left (actually, this is original left only)
        
        current_node = root

        while current_node is not None: # meaning that the tree traversal is not done
            # No left child; just swap and go left
            if current_node.left is None:
                # Swap the nodes now
                swap_node = current_node.left
                current_node.left = current_node.right
                current_node.right = swap_node
                current_node = current_node.left # Continue to what was originally the right

            else:
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
                
        return root