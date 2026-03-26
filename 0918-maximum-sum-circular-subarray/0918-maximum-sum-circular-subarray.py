class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        # Logic: Using Kadanes' Algorithm and Suffix Max Subarray

        arr_len = len(nums)

        max_normal_sub_arr_sum = nums[0]
        max_circular_sub_arr_sum = nums[0]
        prefix_sum = 0
        curr_sub_array_sum = 0

        max_suffix_sum_arr = [0] * (arr_len + 1)

        max_suffix_sum_arr[arr_len - 1] = nums[arr_len - 1]
        max_suffix_sum = nums[arr_len - 1]

        for idx_i in range(arr_len - 2, -1, -1):
            max_suffix_sum += nums[idx_i]
            max_suffix_sum_arr[idx_i] = max(max_suffix_sum, max_suffix_sum_arr[idx_i + 1])
        
        # print('suffix_sum', max_suffix_sum_arr)

        for idx_i in range(arr_len):
            # Kadane's Algo to calculate the maxSubArrSum;
            curr_sub_array_sum = max(curr_sub_array_sum + nums[idx_i], nums[idx_i])
            max_normal_sub_arr_sum = max(max_normal_sub_arr_sum, curr_sub_array_sum)

            # Calculating the maximum circular subArrSum;
            prefix_sum += nums[idx_i]
            max_suffix_sum = max_suffix_sum_arr[idx_i + 1]

            max_circular_sub_arr_sum = max(max_circular_sub_arr_sum, prefix_sum + max_suffix_sum)
            # print('prefix_sum', prefix_sum, curr_sub_array_sum)
            # print('max_sub_arr_sum', max_normal_sub_arr_sum, max_circular_sub_arr_sum)
        
        return max(max_normal_sub_arr_sum, max_circular_sub_arr_sum)
        '''

        '''
        # Optimized Solution using the formula:
        # Total_Arr_Sum - Min_Sub_Arr_Sum

        max_normal_sub_arr_sum = nums[0]
        min_normal_sub_arr_sum = nums[0]
        curr_sub_arr_sum = 0

        # Calculate the total array sum:
        total_arr_sum = sum(nums)

        # Calculate the maximum subarray sum:
        for num in nums:
            curr_sub_arr_sum = max(num + curr_sub_arr_sum, num)

            max_normal_sub_arr_sum = max(max_normal_sub_arr_sum, curr_sub_arr_sum)
        
        curr_sub_arr_sum = 0

        # Calculate the minimum subarray sum:
        for num in nums:
            curr_sub_arr_sum = min(num + curr_sub_arr_sum, num)

            min_normal_sub_arr_sum = min(min_normal_sub_arr_sum, curr_sub_arr_sum)

        # there's no maximum circular sub array sum hence normal subarr sum is the ans;
        if total_arr_sum == min_normal_sub_arr_sum:
            return max_normal_sub_arr_sum

        # there's a maximum circular sub array sum hence return max ans;
        max_sub_arr_sum = total_arr_sum - min_normal_sub_arr_sum
        max_sub_arr_sum = max(max_normal_sub_arr_sum, max_sub_arr_sum)

        return max_sub_arr_sum
        '''

        # Single Pass Solution:
        # Optimized Solution using the formula:
        # Total_Arr_Sum - Min_Sub_Arr_Sum

        max_normal_sub_arr_sum = nums[0]
        min_normal_sub_arr_sum = nums[0]
        curr_max_sub_arr_sum = 0
        curr_min_sub_arr_sum = 0

        total_arr_sum = 0

        for num in nums:
            # Calculate the maximum subarray sum:
            curr_max_sub_arr_sum = max(num + curr_max_sub_arr_sum, num)
            max_normal_sub_arr_sum = max(max_normal_sub_arr_sum, curr_max_sub_arr_sum)

            # Calculate the minimum subarray sum:
            curr_min_sub_arr_sum = min(num + curr_min_sub_arr_sum, num)
            min_normal_sub_arr_sum = min(min_normal_sub_arr_sum, curr_min_sub_arr_sum)
        
            # Calculate the total array sum:
            total_arr_sum += num

        if total_arr_sum == min_normal_sub_arr_sum:
            return max_normal_sub_arr_sum

        max_sub_arr_sum = total_arr_sum - min_normal_sub_arr_sum
        max_sub_arr_sum = max(max_normal_sub_arr_sum, max_sub_arr_sum)

        return max_sub_arr_sum