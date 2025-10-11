class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # #Striver Version Solution
        # Editorial Version Approach 4: 
        # If we calculate the number of subarrays with sum at most k and at most
        # k - 1, their difference would give us the number of subarrays with sum
        # exactly k.
        # Number of subarrays with at most k odd elements is calculated as end - start + 1
        # in the given window size where the odd elements are less than or equals k

        # Logic: Count the number of nice subarrays that are less
        # than or equal to k i.e subArrsLessThanForK and count the number of nice subarrays
        # that are less than or equal to k - 1 i.e subArrsLessThanForPrevK
        # and if you substract the number of subarrays that are less than or equal to k - 1
        # from less than or equal to k then you get the subarrs equals to k
        # niceSubArrsCount = subArrsLessThanForK - subArrsLessThanForPrevK

        # why? just think about it if k = 3 and your countX = 5 
        # and k - 1 = 2 and your countY = 2
        # then you are doing (countX <= 3) - (countY <= 2) so basically you 
        # removing all the subarrays count that are less than to 3 by counting
        #  for less than or equal to k - 1

        def count_nice_subarrs(nums, k):
            window_strt_idx = 0
            nice_subarrs_count = 0

            total_odd_nums = 0

            for window_end_idx in range(len(nums)):
                curr_num = nums[window_end_idx]

                # Odd number count increases;
                if curr_num % 2 != 0:
                    total_odd_nums += 1
                
                while total_odd_nums > k and (window_strt_idx < window_end_idx + 1):
                    if nums[window_strt_idx] % 2 != 0:
                        total_odd_nums -= 1
                    window_strt_idx += 1
                
                nice_subarrs_count += window_end_idx - window_strt_idx + 1
            
            return nice_subarrs_count
            
        nice_subarrs_less_than_k = count_nice_subarrs(nums, k)
        nice_subarrs_less_than_prevk = count_nice_subarrs(nums, k - 1)

        total_nice_subarrs_count = nice_subarrs_less_than_k - nice_subarrs_less_than_prevk

        return total_nice_subarrs_count

        '''
        # Solution 2: Using Hashmap and PrefixSum 
        # Problem is similar to Subarray sum equals k; just replace even value with 0
        # and odd value with 1 & the target is k

        # Equation: prefixSum(i) = prefixSum(j) - k

        total_nice_subarrs_count = 0

        prefix_sum = 0
        prefix_sum_freq_map = {}

        prefix_sum_freq_map[0] = 1

        for num in nums:
            # just adding the even or odd values as 0 & 1
            prefix_sum += (num % 2)

            hash_key = prefix_sum - k
            
            # Add subarrays with sum k ending at this index num;
            if hash_key in prefix_sum_freq_map:
                total_nice_subarrs_count += prefix_sum_freq_map[hash_key]
            
            # increment the current prefix sum in hashmap
            hash_value = prefix_sum_freq_map.get(prefix_sum, 0) + 1
            prefix_sum_freq_map[prefix_sum] = hash_value

        return total_nice_subarrs_count
        '''

