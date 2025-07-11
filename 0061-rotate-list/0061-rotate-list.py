# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Logic: Solution using two pointers reverse array technique
        # and converting the list to an array;
        # When reversing to the right by k steps
        # First need to reverse the entire array,
        # then reverse the first k steps & then the last k steps

        # When reversing to the left by k steps
        # First need to reverse the first k steps & then last k steps
        # Finally, need to reverse the entire array;
        
        if not head:
            return head

        current_node = head
        nodes_arr = []

        while current_node:
            nodes_arr.append(current_node.val)
            current_node = current_node.next

        n = len(nodes_arr)
        k = k % n

        if k == 0:
            return head
        
        def reverse(strt_idx, end_idx):
            while strt_idx < end_idx:
                nodes_arr[strt_idx], nodes_arr[end_idx] = nodes_arr[end_idx], nodes_arr[strt_idx]
                strt_idx += 1
                end_idx -= 1
            
            return
        
        # reverse the entire array;
        reverse(0, n - 1)

        # reverse first k elements;
        reverse(0, k - 1)

        # reverse last k elements
        reverse(k, n - 1)

        # create a new list and that's answer;
        new_head = ListNode(-1)
        current_node = new_head

        for node_val in nodes_arr:
            new_node = ListNode(node_val)
            current_node.next = new_node
            current_node = current_node.next

        new_head = new_head.next
        return new_head