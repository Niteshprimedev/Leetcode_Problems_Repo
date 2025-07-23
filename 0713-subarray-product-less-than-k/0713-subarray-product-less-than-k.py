class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        # Logic: Using the striver's video solution;
        # How the `right - left + 1` formula works?
        # cause it gives us the number of *unique* subarrays ending at "right" index!
        
        # The edge case is valid, cause the subarray product should
        # be strictly less than k, so if k is 1 or 0 then the subarray
        # won't be strictly less than k since we have nums range from 1 to 1000
        if k < 2:
            return 0

        def countSubArrs(nums, k):
            if k < 0:
                return 0
            
            total_subarrs_count = 0
            window_strt_idx = 0
            prefix_product = 1
            
            for window_end_idx in range(len(nums)):
                curr_num = nums[window_end_idx]

                prefix_product *= curr_num

                while window_strt_idx < (window_end_idx + 1) and prefix_product >= k:
                    prefix_product /= nums[window_strt_idx]
                    window_strt_idx += 1
                
                total_subarrs_count += window_end_idx - window_strt_idx + 1
            
            return total_subarrs_count
        
        total_k_subarrs_product = countSubArrs(nums, k)
        return total_k_subarrs_product
        '''

        # Solution 2: Modifying the while condition;
        if k < 2:
            return 0

        def countSubArrs(nums, k):
            if k < 0:
                return 0
            
            total_subarrs_count = 0
            window_strt_idx = 0
            prefix_product = 1
            
            for window_end_idx in range(len(nums)):
                curr_num = nums[window_end_idx]

                prefix_product *= curr_num

                while window_strt_idx <= window_end_idx and prefix_product >= k:
                    prefix_product /= nums[window_strt_idx]
                    window_strt_idx += 1
                
                total_subarrs_count += window_end_idx - window_strt_idx + 1
            
            return total_subarrs_count
        
        total_k_subarrs_product = countSubArrs(nums, k)
        return total_k_subarrs_product


