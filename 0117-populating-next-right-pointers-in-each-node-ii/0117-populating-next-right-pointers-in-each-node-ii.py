"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
         # Starting at root level
        prev_level_root = root

        while True:
            next_level_head = None # Will point to first node of next level
            next_level_tail = None # Will keep linking nodes at next level

            # Traverse current level using .next pointers
            while prev_level_root:
                # Handle left child
                if prev_level_root.left is not None:
                    if next_level_tail is None:
                        next_level_head = prev_level_root.left
                        next_level_tail = prev_level_root.left
                    else:
                        next_level_tail.next = prev_level_root.left
                        next_level_tail = next_level_tail.next
                # Handle right child
                if prev_level_root.right is not None:
                    if next_level_tail is None:
                        next_level_head = prev_level_root.right
                        next_level_tail = prev_level_root.right
                    else:
                        next_level_tail.next = prev_level_root.right
                        next_level_tail = next_level_tail.next
                # Move sideways in current level
                prev_level_root = prev_level_root.next

            # No more levels to process
            if next_level_head is None:
                break

            # Traverse to next level this is to process the 
            # next left child and right child nodes
            prev_level_root = next_level_head
        
        return root