class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Using Kadane's Algorithm to find the max absolute sum;

        max_sub_arr_sum = - float('inf')
        min_sub_arr_sum = float('inf')

        curr_sub_arr_sum = 0

        for idx_i in range(len(nums)):
            num = nums[idx_i]

            curr_sub_arr_sum += num

            max_sub_arr_sum = max(max_sub_arr_sum, curr_sub_arr_sum)

            if curr_sub_arr_sum < 0:
                curr_sub_arr_sum = 0
        
        curr_sub_arr_sum = 0
        
        for idx_j in range(len(nums)):
            num = nums[idx_j]

            curr_sub_arr_sum += num

            min_sub_arr_sum = min(min_sub_arr_sum, curr_sub_arr_sum)

            if curr_sub_arr_sum > 0:
                curr_sub_arr_sum = 0

        return max(abs(max_sub_arr_sum), abs(min_sub_arr_sum))
