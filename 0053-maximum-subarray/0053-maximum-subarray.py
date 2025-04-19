class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memoDP = [0 for _ in range(len(nums))]
        max_sub_arr_sum = nums[0]

        memoDP[0] = nums[0]

        for idx_i in range(1, len(nums)):
            curr_num = nums[idx_i]
            memoDP[idx_i] = max(memoDP[idx_i - 1] + curr_num, curr_num)

            max_sub_arr_sum = max(max_sub_arr_sum, memoDP[idx_i])
        
        return max_sub_arr_sum