# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list_head = ListNode(-1)
        current_node = merged_list_head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            
            current_node = current_node.next
            
        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2
        
        merged_list_head = merged_list_head.next
        return merged_list_head