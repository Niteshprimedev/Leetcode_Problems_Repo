class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Logic: using total flips count logic
        # and if all the elements are one then delete one 1 element

        window_strt_idx = 0

        max_el_del_count = 0

        longest_subarr_len = 0

        for window_end_idx in range(len(nums)):
            curr_num = nums[window_end_idx]

            if curr_num == 0:
                max_el_del_count += 1

            while max_el_del_count > 1 and window_strt_idx < window_end_idx + 1:
                if nums[window_strt_idx] == 0:
                    max_el_del_count -= 1
                window_strt_idx += 1
            
            window_size = window_end_idx - window_strt_idx

            longest_subarr_len = max(longest_subarr_len, window_size)

        return longest_subarr_len

        '''
        # Solution 2: Optimal Solution;
        # Logic: Expand the window as long as the condition is valid
        # and then maintain the longest window as long as the condition is invalid
        # if the window has longest window further down the line then it will update;
        # Expand but don't shrink just maintain the window;

        window_strt_idx = 0
        longest_subarr_len = 0

        max_del_count = 0

        for window_end_idx in range(len(nums)):
            curr_num = nums[window_end_idx]

            if curr_num == 0:
                max_del_count += 1

            if max_del_count > 1:
                if nums[window_strt_idx] == 0:
                    max_del_count -= 1
                
                window_strt_idx += 1
            
            # deleting 1 element so no need to add 1;
            window_size = window_end_idx - window_strt_idx

            longest_subarr_len = max(longest_subarr_len, window_size)
        
        return longest_subarr_len
        '''