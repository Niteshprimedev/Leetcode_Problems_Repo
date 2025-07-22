class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        # Logic: Solution1 using Sliding window where
        # the subarrs are counted whenever there are k or
        # less than k distinct elements: So compute subarrs for k - 1
        # distinct element and compute subarrs for k distinct elements
        # then substract the k - 1 from k to get k size subarrs;
        
        def count_subarrs(nums, target):
            # we can't have subarrs with 0 dist integers
            if target <= 0:
                return 0

            window_strt_idx = 0
            total_subarrs_count = 0
            nums_els_map = {}
            
            for window_end_idx in range(len(nums)):
                curr_num = nums[window_end_idx]
                
                if curr_num not in nums_els_map:
                    nums_els_map[curr_num] = 0
                    
                nums_els_map[curr_num] += 1
                
                # shrink the window as the window is invalid
                while len(nums_els_map) > target and window_strt_idx < window_end_idx + 1:
                    strt_num = nums[window_strt_idx]
                    
                    nums_els_map[strt_num] -= 1
                    
                    if nums_els_map[strt_num] == 0:
                        nums_els_map.pop(strt_num, None)
                        
                    window_strt_idx += 1
                    
                # count total substrings smaller than or equal to target
                total_subarrs_count += window_end_idx - window_strt_idx + 1
            
            return total_subarrs_count
        
        total_subarrs_smaller_and_equal_k = count_subarrs(nums, k)
        total_subarrs_smaller_k = count_subarrs(nums, k - 1)
        
        total_subarrs_equal_k = total_subarrs_smaller_and_equal_k - total_subarrs_smaller_k
        
        return total_subarrs_equal_k
        '''
        
        # Logic: Solution using Sliding window where
        # the subarrs are counted whenever there are k or
        # less than k distinct elements: So compute subarrs for k - 1
        # distinct element and compute subarrs for k distinct elements
        # then substract the k - 1 from k to get k size subarrs;
        
        def count_subarrs(nums, target):
            # we can't have subarrs with 0 dist integers
            if target <= 0:
                return 0

            window_strt_idx = 0
            total_subarrs_count = 0
            nums_els_map = {}
            
            for window_end_idx in range(len(nums)):
                curr_num = nums[window_end_idx]
                
                if curr_num not in nums_els_map:
                    nums_els_map[curr_num] = 0
                    
                nums_els_map[curr_num] += 1
                
                # shrink the window as the window is invalid
                while len(nums_els_map) > target and window_strt_idx <= window_end_idx:
                    strt_num = nums[window_strt_idx]
                    
                    nums_els_map[strt_num] -= 1
                    
                    if nums_els_map[strt_num] == 0:
                        nums_els_map.pop(strt_num, None)
                        
                    window_strt_idx += 1
                    
                # count total subarrays smaller than or equal to target
                total_subarrs_count += window_end_idx - window_strt_idx + 1
            
            return total_subarrs_count
        
        total_subarrs_smaller_and_equal_k = count_subarrs(nums, k)
        total_subarrs_smaller_k = count_subarrs(nums, k - 1)
        
        total_subarrs_equal_k = total_subarrs_smaller_and_equal_k - total_subarrs_smaller_k
        
        return total_subarrs_equal_k