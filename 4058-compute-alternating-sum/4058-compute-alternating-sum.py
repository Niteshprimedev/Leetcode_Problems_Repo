class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        alt_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                alt_sum += nums[i] 
            else:
                alt_sum -= nums[i]
            
        return alt_sum