# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_val = 0
        current_node = head

        length = 0

        while current_node:
            length += 1
            current_node = current_node.next

        # print(length)
        current_node = head

        while current_node:
            length -= 1
            decimal_val = decimal_val | (current_node.val << length)
            # print(current_node.val << length)
            current_node = current_node.next

        return decimal_val
        