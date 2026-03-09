# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Logic: Find (k-1)th node and then reset the
        # pointers to remove the kth node;
        if n <= 0 or head == None:
            return head
        
        if head.next == None and n == 1:
            return head.next
        
        slow_node = head
        fast_node = head
        prev_node = None

        # move fast_node by n - 1 step ahead in the list;
        for node_idx in range(n):
            if fast_node:
                fast_node = fast_node.next
        
        if fast_node == None:
            return head.next
        
        while fast_node:
            prev_node = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next

        prev_node.next = slow_node.next
        slow_node.next = None

        return head