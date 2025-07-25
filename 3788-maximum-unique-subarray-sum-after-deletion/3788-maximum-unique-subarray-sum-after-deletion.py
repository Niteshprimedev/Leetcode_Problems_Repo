class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_els = set(nums)

        curr_sub_arr_sum = 0
        max_sub_arr_sum = -101

        for num in unique_els:
            if num < 0:
                max_sub_arr_sum = max(max_sub_arr_sum, num)
                continue
                
            curr_sub_arr_sum = max(curr_sub_arr_sum + num, num)
            max_sub_arr_sum = max(max_sub_arr_sum, curr_sub_arr_sum)
        
        return max_sub_arr_sum