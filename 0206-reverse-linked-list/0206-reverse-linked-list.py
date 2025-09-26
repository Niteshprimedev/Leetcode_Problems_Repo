# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
class DSANode:
    def __init__(self, val, next):
        self.val = val
        self.next = None
    

def connections(self):
'''
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        # Home Work:
        node_a = DSANode(5)
        node_b = DSANode(6)
        node_c = DSANode(7)

        # connections:
        node_a.next = node_b
        node_b.next = node_c
        '''

        '''
        def reverse_list(head):
            # 1. stop on empty list OR single node
            if head is None or head.next is None:
                return head

            # 2. reverse the rest
            new_head = reverse_list(head.next)

            # 4.5.next = None (this is already None) so now attach 4 to it;
            # 4.5.next = 4 and 4.next = None

            # 3. put 'head' at the end of the reversed sub-list
            head.next.next = head   # old next node now points to head
            head.next = None        # detach head

            return new_head         # new_head is the head of the whole reversed list
        
        return reverse_list(head)
        '''

        # Recursive Solution Discussed in the class: DSA Session 7
        def reverse_list(head):
            # Base Case:
            if head == None or head.next == None:
                return head

            # get the new_head of the linked list
            new_head = reverse_list(head.next)

            # Attach the current_head to the tail of the linked list new_head
            current_node = new_head

            while current_node.next:
                current_node = current_node.next

            current_node.next = head

            # disconnect the head.next pointer cause it's part of the reverse list
            head.next = None

            # return the new_head of the linked list;
            return new_head
        
        return reverse_list(head)
        
        '''
        def reverse_list(head):
            # Base Case:
            if head == None or head.next == None:
                return head

            # get the new_head of the linked list
            new_head = reverse_list(head.next)

            # Attach the current_head to the tail of the linked list new_head
            current_node = new_head

            while current_node.next:
                current_node = current_node.next

            current_node.next = head

            # disconnect the head.next pointer cause it's part of the reverse list
            head.next = None

            # return the new_head of the linked list;
            return new_head
        
        return reverse_list(head)
        '''   
        