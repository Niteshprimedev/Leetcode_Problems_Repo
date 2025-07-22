class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        # Solution 1: TLE
        # Logic: Sliding Window -> Expand the window
        # as long asa you have unique elements in window
        # else shrink the window;

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        hash_map_arr = [-1] * (10**4 + 1)
        max_erasure_val = 0
        max_window_size = [0, 0]

        strt_idx = 0

        def calc_max_erasure_sum(strt_idx, end_idx):
            max_erasure_val = 0

            # Compute the max_erasure_val of the max_window_size
            for idx in range(strt_idx, end_idx + 1):
                curr_num = nums[idx]
                max_erasure_val += curr_num
            
            return max_erasure_val
            
        for end_idx in range(len(nums)):
            curr_num = nums[end_idx]

            # Shrink the window as duplicate encountered
            if hash_map_arr[curr_num] != -1:
                hash_value = hash_map_arr[curr_num]

                if hash_value + 1 > strt_idx:
                    strt_idx = hash_value + 1

            # Expand the window as unique window so far
            hash_map_arr[curr_num] = end_idx

            # Calculate prev_window_size and curr_window_size
            prev_window_size = max_window_size[1] - max_window_size[0] + 1
            curr_window_size = end_idx - strt_idx + 1

            # Update the max_window_size if a new max is found;
            if curr_window_size > prev_window_size:
                max_window_size = [end_idx, strt_idx]
                max_erasure_val = max(max_erasure_val, calc_max_erasure_sum(strt_idx, end_idx))
        

        return max_erasure_val
        '''
        
        '''
        # Solution 2: Optimized using Nested loops & Freq
        # Logic: Sliding Window -> Expand the window
        # as long asa you have unique elements in window
        # else shrink the window;

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        hash_map_arr = [0] * (10**4 + 1)
        max_erasure_val = 0
        curr_erasure_val = 0

        strt_idx = 0

        for end_idx in range(len(nums)):
            curr_num = nums[end_idx]

            # Expand the window as unique window so far
            curr_erasure_val += curr_num
            hash_map_arr[curr_num] += 1
            
            # Shrink the window as duplicate encountered
            while strt_idx <= end_idx and hash_map_arr[curr_num] > 1:
                strt_num = nums[strt_idx]

                curr_erasure_val -= strt_num
                hash_map_arr[strt_num] -= 1
                strt_idx += 1

            # Update the max_window_size if a new max is found;
            max_erasure_val = max(max_erasure_val, curr_erasure_val)

        return max_erasure_val
        '''

        '''
        # Solution 3: Optimized using Nested loops & Indexing
        # Simiilar to Longest Substring without Repeating chars;
        # Logic: Sliding Window -> Expand the window
        # as long asa you have unique elements in window
        # else shrink the window;

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        hash_map_arr = [-1] * (10**4 + 1)
        max_erasure_val = 0
        curr_erasure_val = 0

        strt_idx = 0

        for end_idx in range(len(nums)):
            curr_num = nums[end_idx]
          
            # Shrink the window as duplicate encountered
            if hash_map_arr[curr_num] != -1:
                while strt_idx <= hash_map_arr[curr_num]:
                    strt_num = nums[strt_idx]

                    curr_erasure_val -= strt_num
                    hash_map_arr[strt_num] -= 1
                    strt_idx += 1
            
            # Expand the window as unique window so far
            curr_erasure_val += curr_num
            hash_map_arr[curr_num] = end_idx

            # Update the max_window_size if a new max is found;
            max_erasure_val = max(max_erasure_val, curr_erasure_val)

        return max_erasure_val
        '''

        # Solution 4: Optimized using Nested loops & Duplicates arr
        # Simiilar to Longest Substring without Repeating chars;
        # Logic: Sliding Window -> Expand the window
        # as long asa you have unique elements in window
        # else shrink the window;

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        is_duplicate = [False] * (10**4 + 1)
        max_erasure_val = 0
        curr_erasure_val = 0

        strt_idx = 0

        for end_idx in range(len(nums)):
            curr_num = nums[end_idx]
          
            # Shrink the window as duplicate encountered
            while is_duplicate[curr_num]:
                strt_num = nums[strt_idx]

                curr_erasure_val -= strt_num
                is_duplicate[strt_num] = False
                strt_idx += 1
            
            # Expand the window as unique window so far
            curr_erasure_val += curr_num
            is_duplicate[curr_num] = True

            # Update the max_window_size if a new max is found;
            max_erasure_val = max(max_erasure_val, curr_erasure_val)

        return max_erasure_val