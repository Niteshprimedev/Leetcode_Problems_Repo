class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        '''
        # Observation:
        # Smallest Subarray with maximum Bitwise OR;
        # Shrink then XOR to cancel out the bits value
        # Expanding then OR to accumulate the bits value
        
        # Intuition: Compute the bitwise OR of the entire array
        # this is the target of our window, so expand the window
        # as long as the bitwise target is not reached and then
        # Shrink the window once you hit the target
        # Note: You also need to update the target value by removing
        # the set bits at the curr_idx to have a valid target for the
        # subarray starting at i + 1 

        curr_bitwise_val = 0

        n = len(nums)
        smallest_subarrs = [0] * n

        for idx in range(n - 1, -1, -1):
            num = nums[idx]
            curr_bitwise_val |= num

            smallest_subarrs[idx] = curr_bitwise_val
        
        window_strt_idx = 0
        window_end_idx = 0
        curr_bitwise_val = 0

        while window_end_idx < n:
            curr_num = nums[window_end_idx]

            curr_bitwise_val |= curr_num

            if curr_bitwise_val == smallest_subarrs[window_strt_idx]:
                window_size = window_end_idx - window_strt_idx + 1
                
                print(window_strt_idx, window_size, window_end_idx)
                print(curr_bitwise_val)
                
                while window_strt_idx < window_end_idx:
                    smallest_subarrs[window_strt_idx] = window_size

                    window_strt_idx += 1
                
                curr_bitwise_val = curr_num

            window_end_idx += 1
        
        return smallest_subarrs        
        # return [6,5,4,3,2,1]
        '''
        last = [-1] * 32
        for i in range(len(nums) - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i
            nums[i] = max(1, max(last) - i + 1)
        return nums