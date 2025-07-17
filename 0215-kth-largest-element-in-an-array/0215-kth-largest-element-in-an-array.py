class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        # Solved after DSA Session 12 on June 8th;
        # Logic: Use heap to store the kth largest elements;
        # Min-Heap Solution; So idea is to use min heap for largest
        # greatest, biggest, and longest
        # Use Max-Heap Solution; when smallest;

        # Left Child Formula: 
        # idx multiply by 2 and add 1 to it;

        heap = []
        nums_len = len(nums)

        def swap_nodes(heap_tree, node1, node2):
            # these are not nodes but indices;
            heap_tree[node1], heap_tree[node2] = heap_tree[node2], heap_tree[node1]
            return heap_tree

        def heapify_up(heap_tree):
            # Left Child Formula: 
            # idx multiply by 2 and add 1 to it;
            heap_size = len(heap_tree)

            for parent_idx in range(heap_size - 1, -1, -1):
                left_child_idx = (2 * parent_idx) + 1
                
                if left_child_idx >= heap_size:
                    continue
                
                right_child_idx = (2 * parent_idx) + 2

                smaller_child_idx = left_child_idx

                if right_child_idx < heap_size and heap_tree[right_child_idx] < heap_tree[left_child_idx]:
                    smaller_child_idx = right_child_idx
                
                if heap_tree[parent_idx] > heap_tree[smaller_child_idx]:
                    swap_nodes(heap_tree, parent_idx, smaller_child_idx)
            
            return heap_tree

        def heapify_down(heap_tree):
            # Left Child Formula: 
            # idx multiply by 2 and add 1 to it;
            heap_size = len(heap_tree)

            for parent_idx in range(heap_size):
                left_child_idx = (2 * parent_idx) + 1
                
                if left_child_idx >= heap_size:
                    continue
                
                right_child_idx = (2 * parent_idx) + 2

                smaller_child_idx = left_child_idx

                if right_child_idx < heap_size and heap_tree[right_child_idx] < heap_tree[left_child_idx]:
                    smaller_child_idx = right_child_idx
                
                if heap_tree[parent_idx] > heap_tree[smaller_child_idx]:
                    swap_nodes(heap_tree, parent_idx, smaller_child_idx)
            
            return heap_tree
        
        def delete_node(heap_tree, node_idx):
            heap_size = len(heap_tree)

            swap_nodes(heap_tree, 0, heap_size - 1)
            heap_tree.pop()

            heapify_down(heap_tree)

            return heap_tree


        for idx_i in range(k):
            # Swap when the child is smaller; cause smallest child
            # should be the at the top
            curr_num = nums[idx_i]
            heap.append(curr_num)

            # heapify the tree;
            heapify_up(heap)

        # print(heap)

        for idx_i in range(k, nums_len):
            curr_num = nums[idx_i]

            if heap[0] < curr_num:
                delete_node(heap, 0)

                # then add the curr_num to the top;
                heap.append(curr_num)

                # and heapify the heap tree
                heapify_up(heap)
        
        largest_arr_el = heap[0]

        # print(heap)
        return largest_arr_el
        '''

        '''
        heap = []

        import heapq

        for idx_i in range(k):
            curr_num = nums[idx_i]
            heap.append(curr_num)
        
        heapq.heapify(heap)
        # print(heap)

        for idx_i in range(k, len(nums)):
            heapq.heappush(heap, nums[idx_i])
            # print(heap)
            heapq.heappop(heap)

        return heap[0]
        '''

        '''
        priority_q = []
        
        for idx_i in range(k):
            curr_num = nums[idx_i]
            heapq.heappush(priority_q, curr_num)
        
        for idx_i in range(k, len(nums)):
            curr_num = nums[idx_i]
            curr_min = heapq.heappop(priority_q)
            heapq.heappush(priority_q, max(curr_min, curr_num))
        
        return priority_q[0]
        '''

        '''
        # Solution 4: Single Loop SOLUTION;
        # Pop the element from the priority_q when the pq size
        # becomes equals to the k elements and then push the max
        # of current_el and the popped element from pq;
        
        priority_q = []

        for idx_i in range(len(nums)):
            curr_num = nums[idx_i]

            if len(priority_q) == k:
                curr_min = heapq.heappop(priority_q)
                curr_num = max(curr_min, curr_num)

            heapq.heappush(priority_q, curr_num)
        
        return priority_q[0]
        '''

        # Solution 5: Single Loop SOLUTION;
        # Pop the min element from the priority_q when the pq size
        # greater than the k elements 

        priority_q = []

        for num in nums:
            heapq.heappush(priority_q, num)

            if len(priority_q) > k:
                heapq.heappop(priority_q)
        
        return priority_q[0]
