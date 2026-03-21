class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force Solution:
        # That is generating all possible subarrays 
        # and calculating their sum, if sum is equal to 
        # target then we found our subarray
        
        # Another technique to solve is below:
        # Classic subarrays sum equal target or k 
        # Solution using Prefix Sum and Hashmap;
        '''
        // PrefixSum & Hashmap Approach
        // Hint4: sum(i, j) = sum(0, j) - sum(0, i), where sum(i, j) represents the sum
        // of all the elements from index i to j - 1.
        // Can we use this property to optimize it?

        // Equation?
        // subArrSum(i - 1) = subArrSum(j) - k;
        '''
        
        total_given_sum_subarrs_count = 0
        
        prefix_sum_freq_map = {}
        prefix_sum_freq_map[0] = 1
        
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            
            hash_key = prefix_sum - k
            
            if hash_key in prefix_sum_freq_map:
                total_given_sum_subarrs_count += prefix_sum_freq_map[hash_key]
        
            hash_value = prefix_sum_freq_map.get(prefix_sum, 0) + 1
            prefix_sum_freq_map[prefix_sum] = hash_value
        
        return total_given_sum_subarrs_count

        '''
        # Logic: To find the longest subarray that 
        # is equal to given sum, we just need to store the
        # first idx of the prefix_sum and ignore the 
        # remaining repeated prefix_sums cause that will give us
        # longest subarray length;
        longest_given_sum_subarray = 0
        
        prefix_sum_freq_map = {}
        prefix_sum_freq_map[0] = -1
                
        prefix_sum = 0
        
        for num_idx in range(len(nums)):
            num = nums[num_idx]
            prefix_sum += num
            
            hash_key = prefix_sum - k
            
            if hash_key in prefix_sum_freq_map:
                subarr_strt_idx = prefix_sum_freq_map[hash_key]
                subarr_end_idx = num_idx

                new_longest_given_sum_subarray = subarr_end_idx - subarr_strt_idx
                longest_given_sum_subarray = max(longest_given_sum_subarray, new_longest_given_sum_subarray)
            
            if prefix_sum not in prefix_sum_freq_map:
                prefix_sum_freq_map[prefix_sum] = num_idx
        
        return longest_given_sum_subarray
        '''