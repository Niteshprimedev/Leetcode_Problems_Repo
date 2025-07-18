class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        # Logic: Use the max_heap from the start to find
        # the minimum sum of n elements
        # Use the min_heap from the end to find the maximum 
        # sum of n elements and take the difference;

        n = len(nums)
        division_count = n // 3
        
        # -------- Suffix part --------
        end_min_heap = []
        end_n_els_sum = 0
        max_suffix_sum = [0] * n

        for idx in range(n-1, division_count-1, -1):
            end_n_els_sum += nums[idx]
            heapq.heappush(end_min_heap, nums[idx])

            if len(end_min_heap) > division_count:
                end_n_els_sum -= heapq.heappop(end_min_heap)
            # store max sum of n elements from idx..end
            if idx == n-1:
                max_suffix_sum[idx] = end_n_els_sum
            else:
                max_suffix_sum[idx] = max(max_suffix_sum[idx+1], end_n_els_sum)
            
        # print(max_suffix_sum)

        # -------- Prefix part --------
        loop_len = n - division_count
        strt_max_heap = []
        first_n_els_sum = 0
        min_sums_diff = float('inf')

        for idx in range(loop_len):  # iterate first 2n
            first_n_els_sum += nums[idx]
            heapq.heappush(strt_max_heap, -nums[idx])

            if len(strt_max_heap) > division_count:
                first_n_els_sum -= -heapq.heappop(strt_max_heap)

            if idx >= division_count-1:
                # suffix starts at idx+1
                new_min_sums_diff = first_n_els_sum - max_suffix_sum[idx + 1]
                min_sums_diff = min(min_sums_diff, new_min_sums_diff)

        return min_sums_diff
        '''
        
        '''
        # Solution 2: Fixed Issue in calculating the min_diff;
        # Logic: Use the max_heap from the start to find
        # the minimum sum of n elements
        # Use the min_heap from the end to find the maximum 
        # sum of n elements and take the min difference;

        n = len(nums)
        division_count = n // 3
        
        # -------- Suffix part --------
        end_min_heap = []
        max_suffix_sum = [0] * n
        end_n_els_sum = 0
        first_part_last_idx = division_count - 1

        for idx in range(n - 1, first_part_last_idx, -1):
            end_num = nums[idx]

            end_n_els_sum += end_num
            heapq.heappush(end_min_heap, end_num)

            if len(end_min_heap) > division_count:
                end_n_els_sum -= heapq.heappop(end_min_heap)

            if idx == (n - 1): 
                # max_suffix sum for last idx is last val itself;
                max_suffix_sum[idx] = end_num
            else:
                max_suffix_sum[idx] = max(max_suffix_sum[idx + 1], end_n_els_sum)
        
        # print(max_suffix_sum)

        # -------- Prefix part --------
        
        first_n_els_sum = 0
        strt_max_heap = []
        loop_len = n - division_count
        
        min_sums_diff = float('inf')

        for idx_i in range(loop_len):
            strt_num = nums[idx_i]

            heapq.heappush(strt_max_heap, -strt_num)

            first_n_els_sum += strt_num

            if len(strt_max_heap) > division_count:
                first_n_els_sum -= abs(heapq.heappop(strt_max_heap))

            # skip the first n elements and then compute
            # minSum - maxSum
            if idx_i >= first_part_last_idx:
                next_n_els_sum = max_suffix_sum[idx_i + 1]
                new_min_sums_diff = first_n_els_sum - next_n_els_sum
                min_sums_diff = min(min_sums_diff, new_min_sums_diff)
            
        return min_sums_diff
        '''

        # Solution 3: Commented Code;
        n = len(nums)
        group_size = n // 3  # we need to remove exactly n elements from 3n
        total_len_for_loop = 2 * group_size  # we'll process first 2n elements

        # ------------------------------
        # Step 1: Compute max_suffix_sum
        # max_suffix_sum[i] = the maximum sum of `group_size` elements
        # we can choose from nums[i ... n-1]
        # ------------------------------
        suffix_min_heap = []        # will hold n elements from end, as a min-heap
        current_suffix_sum = 0
        max_suffix_sum = [0] * n    # suffix array to store max sums

        # build suffix sums from right to left
        for idx in range(n - 1, group_size - 1, -1):
            current_suffix_sum += nums[idx]
            heapq.heappush(suffix_min_heap, nums[idx])

            # if we took more than n elements, remove the smallest
            if len(suffix_min_heap) > group_size:
                current_suffix_sum -= heapq.heappop(suffix_min_heap)
            # fill max_suffix_sum for this index
            if idx == n - 1:
                max_suffix_sum[idx] = current_suffix_sum
            else:
                max_suffix_sum[idx] = max(max_suffix_sum[idx + 1], current_suffix_sum)

        # ------------------------------
        # Step 2: Process prefix and track minimal difference
        # prefix_max_heap will help us keep track of n smallest prefix elements
        # but we store them as negatives to simulate a max-heap
        # ------------------------------
        prefix_max_heap = []        # will hold n elements as negative values
        current_prefix_sum = 0
        min_sum_diff = float('inf')

        for idx in range(total_len_for_loop):
            # add current element to prefix sum
            current_prefix_sum += nums[idx]
            heapq.heappush(prefix_max_heap, -nums[idx])  # push as negative

            # if we exceed group_size, remove the largest element
            if len(prefix_max_heap) > group_size:
                # heappop gives the most negative (largest original),
                # subtract its original value from the prefix sum
                current_prefix_sum -= -heapq.heappop(prefix_max_heap)

            # once we've considered at least group_size elements, compute diff
            if idx >= group_size - 1:
                # we split after idx, suffix starts at idx+1
                best_suffix_sum = max_suffix_sum[idx + 1]
                curr_sum_diff = current_prefix_sum - best_suffix_sum
                min_sum_diff = min(min_sum_diff, curr_sum_diff)

        return min_sum_diff


            
        