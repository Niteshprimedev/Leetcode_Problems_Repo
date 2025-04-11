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
        last_level_head = root

        while True:
            next_level_head = None # Will point to first node of next level
            next_level_tail = None # Will keep linking nodes at next level

            # Traverse current level using .next pointers
            while last_level_head:
                # Handle left child
                if last_level_head.left is not None:
                    if next_level_tail is None:
                        next_level_head = last_level_head.left
                        next_level_tail = last_level_head.left
                    else:
                        next_level_tail.next = last_level_head.left
                        next_level_tail = next_level_tail.next
                # Handle right child
                if last_level_head.right is not None:
                    if next_level_tail is None:
                        next_level_head = last_level_head.right
                        next_level_tail = last_level_head.right
                    else:
                        next_level_tail.next = last_level_head.right
                        next_level_tail = next_level_tail.next
                # Move sideways in current level
                last_level_head = last_level_head.next

            # No more levels to process
            if next_level_head is None:
                break

            # Traverse to next level this is to process the 
            # next left child and right child nodes
            last_level_head = next_level_head
        
        return root