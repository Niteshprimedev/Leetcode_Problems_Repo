# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersect_node = None

        nodesA_map = dict()
        current_nodeA = headA
        current_nodeB = headB

        while current_nodeA is not None:
            nodesA_map[current_nodeA] = True

            current_nodeA = current_nodeA.next

        while current_nodeB is not None:
            
            if current_nodeB in nodesA_map:
                intersect_node = current_nodeB
                break
            
            current_nodeB = current_nodeB.next
        
        return intersect_node
            

