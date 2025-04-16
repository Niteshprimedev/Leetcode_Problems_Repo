# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersect_node = None

        # nodesA_map = dict()
        current_nodeA = headA
        current_nodeB = headB

        # Traverse both lists
        while current_nodeA != current_nodeB:
            # Switch to other head when end is reached
            current_nodeA = current_nodeA.next if current_nodeA is not None else headB
            current_nodeB =  current_nodeB.next if current_nodeB is not None else headA
        
        # Either the intersection node or None
        intersect_node = current_nodeB
        return intersect_node

        # Dry Run:
        # headA => 4 -> 5 -> 9 -> 8 -> 6 -> null
        # headB => 3 -> 2 -> 8 -> 6 -> null

        # nodeA => 4 5 9 8 6 null so it resets to headB 3 2 8 and boom they intersect at node 8
        # nodeB => 3 2 8 6 null 4 so it resets to headA 5 9 8 and bam they intersect at node 8

        

