# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Solution 1: Using min_heap and priority queue 
        sorted_list_head = ListNode(-1)
        sorted_list_p = sorted_list_head

        import heapq

        min_heap = []

        for idx_i, linked_list in enumerate(lists):
            current_node = linked_list
            if current_node:
                heapq.heappush(min_heap, (current_node.val, idx_i, current_node))
        
        while len(min_heap) > 0:
            current_node_val, idx_i, current_node = heapq.heappop(min_heap)

            sorted_list_p.next = current_node
            sorted_list_p = sorted_list_p.next

            next_node = current_node.next

            if next_node:
                heapq.heappush(min_heap, (next_node.val, idx_i, next_node))

        sorted_list_head = sorted_list_head.next
        return sorted_list_head

        '''
        # Solution 2: Using Divide and conquer Method;
        # Merge Two Sorted lists method;
        def merge_two_lists(list1, list2):
            merged_list_head = ListNode(-1)
            current_node = merged_list_head

            while list1 and list2:
                if list1.val < list2.val:
                    current_node.next = list1
                    list1 = list1.next
                else:
                    current_node.next = list2
                    list2 = list2.next
                
                current_node = current_node.next
            
            if list1:
                current_node.next = list1
            if list2:
                current_node.next = list2
            
            return merged_list_head.next

        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for idx_i in range(0, len(lists), 2):
                list1 = lists[idx_i]
                list2 = lists[idx_i + 1] if (idx_i + 1) < len(lists) else None

                merged_lists.append(merge_two_lists(list1, list2))
            
            lists = merged_lists
        
        return lists[0]
        '''
