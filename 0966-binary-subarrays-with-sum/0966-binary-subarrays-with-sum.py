class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        # Logic: Using the function to find the subarrs with 
        # goal and goal - 1;

        def count_subarrs(nums, goal):
            if goal < 0:
                return 0

            strt_idx = 0
            end_idx = 0
            curr_sum = 0
            total_subarrs = 0            

            while(end_idx < len(nums)):
                curr_sum += nums[end_idx]

                while (curr_sum > goal and strt_idx <= end_idx):
                    curr_sum -= nums[strt_idx]
                    strt_idx += 1
                
                total_subarrs += end_idx - strt_idx + 1
                end_idx += 1
            
            return total_subarrs
        

        subarrs_with_sum_less_and_equals_goal = count_subarrs(nums, goal - 1)
        subarrs_with_sum_equals_goal = count_subarrs(nums, goal)

        total_subarrs = subarrs_with_sum_equals_goal - subarrs_with_sum_less_and_equals_goal

        return total_subarrs
        '''
        
        total_nice_subarrs = 0
        prefix_sum = 0
        prefix_sum_freq_map = {}

        prefix_sum_freq_map[0] = 1

        for num in nums:
            prefix_sum += num

            hash_key = prefix_sum - goal

            if hash_key in prefix_sum_freq_map:
                total_nice_subarrs += prefix_sum_freq_map[hash_key]
            
            hash_value = prefix_sum_freq_map.get(prefix_sum, 0) + 1
            prefix_sum_freq_map[prefix_sum] = hash_value

        return total_nice_subarrs
