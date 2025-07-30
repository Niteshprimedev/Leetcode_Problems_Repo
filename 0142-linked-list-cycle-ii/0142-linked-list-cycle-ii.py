# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # Solved during DSA Session 7:
        slow = head
        fast = head

        is_cycle_present = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                is_cycle_present = True
                break
            
        if is_cycle_present == False:
            return None

        slow = head
        cyclic_node = fast

        # Find the first node of the cycle;
        while slow != fast:
            slow = slow.next
            fast = fast.next
            cyclic_node = fast
        
        return cyclic_node
        '''

        # Solved during DSA Session 7:
        slow = head
        fast = head

        is_cycle_present = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                is_cycle_present = True
                break
            
        if is_cycle_present == False:
            return None

        slow = head

        # Find the first node of the cycle;
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast

        