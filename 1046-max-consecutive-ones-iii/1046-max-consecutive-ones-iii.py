class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        # Solution on May 11 after DSA Sliding Window Pattern Session
        total_flips_count = 0

        window_strt_idx = 0
        max_cons_ones_arr_len = 0

        for window_end_idx in range(len(nums)):
            curr_num = nums[window_end_idx]

            if curr_num == 0:
                total_flips_count += 1
            
            while total_flips_count > k and window_strt_idx < window_end_idx + 1:
                # shrink the window:
                if nums[window_strt_idx] == 0:
                    total_flips_count -= 1
                window_strt_idx += 1
            
            # valid window length and maximizing it
            max_cons_ones_arr_len = max(max_cons_ones_arr_len, window_end_idx - window_strt_idx + 1)
        
        return max_cons_ones_arr_len
        '''

        # Logic: Expand the window as long flips count is less than or equal to k
        # and then just maintain the window size until the flips count
        # becomes less than or equal to k; and again update the result

        # Solution 2: Most Optimal Solution:
        # Logic: to maintain the window of max_len throughout the traversal
        # and this way it can reduce the extra while loop;
        # solution ref: striver bhaiya videos

        window_strt_idx = 0
        max_cons_ones_arr_len = 0

        total_flips_count = 0

        for window_end_idx in range(len(nums)):
            curr_num = nums[window_end_idx]

            if curr_num == 0:
                total_flips_count += 1
            
            if total_flips_count > k:
                if nums[window_strt_idx] == 0:
                    total_flips_count -= 1
                window_strt_idx += 1
            else:
                window_size = window_end_idx - window_strt_idx + 1

                max_cons_ones_arr_len = max(max_cons_ones_arr_len, window_size)
            
        return max_cons_ones_arr_len