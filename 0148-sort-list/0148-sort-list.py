# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Logic: Sorting & Constructing a Linked List
        # Merge sort on the array data structure and then a new list;

        nodes_val = []

        current_node = head

        while current_node:
            nodes_val.append(current_node.val)
            current_node = current_node.next
        
        def merge(nums, strt, mid, end):
            merged_arr = []
            idx_i = strt
            idx_j = mid + 1

            while idx_i <= mid and idx_j <= end:
                if nums[idx_i] <= nums[idx_j]:
                    merged_arr.append(nums[idx_i])
                    idx_i += 1
                else:
                    merged_arr.append(nums[idx_j])
                    idx_j += 1
            
            while idx_i <= mid:
                merged_arr.append(nums[idx_i])
                idx_i += 1
            while idx_j <= end:
                merged_arr.append(nums[idx_j])
                idx_j += 1
            
            for idx in range(len(merged_arr)):
                nums[idx + strt] = merged_arr[idx]
            
            return nums
        
        def merge_sort(nums, strt, end):
            if strt < end:
                mid = strt + (end - strt) // 2

                merge_sort(nums, strt, mid)                   
                merge_sort(nums, mid + 1, end)

                merge(nums, strt, mid, end)
            
            return nums
        
        merge_sort(nodes_val, 0, len(nodes_val) - 1)

        new_head = ListNode(0)

        sorted_nodes = new_head

        for idx_i in range(len(nodes_val)):
            curr_val = nodes_val[idx_i]
            
            new_node = ListNode(curr_val)
            sorted_nodes.next = new_node
            sorted_nodes = sorted_nodes.next
        
        new_head = new_head.next
        return new_head



        