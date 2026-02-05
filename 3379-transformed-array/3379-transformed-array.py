class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            curr_num = nums[i]

            result_num = 0

            strt_pos = i + curr_num

            if curr_num > 0:
                new_num = strt_pos % n
                result_num = nums[new_num]
            else:
                new_num = (n + strt_pos) % n
                result_num = nums[new_num]
                
            result.append(result_num)
        
        return result