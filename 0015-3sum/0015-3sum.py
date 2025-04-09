class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_sum_equals_zero = []

        nums.sort()
        arr_len = len(nums)

        for first_num_idx in range(arr_len - 2):
            first_num = nums[first_num_idx]
            if first_num_idx > 0 and nums[first_num_idx - 1] == first_num:
                continue
            
            second_num_idx = first_num_idx + 1
            third_num_idx = arr_len - 1

            while second_num_idx < third_num_idx:
                second_num = nums[second_num_idx]
                third_num = nums[third_num_idx]

                triplets_sum = first_num + second_num + third_num
                if triplets_sum == 0:
                    triplets_sum_equals_zero.append([first_num, second_num, third_num])
                    second_num_idx += 1
                    third_num_idx -= 1

                    while second_num_idx < third_num_idx and nums[second_num_idx] == second_num:
                        second_num_idx += 1
                    
                if triplets_sum < 0:
                    second_num_idx += 1
                if triplets_sum > 0:
                    third_num_idx -= 1
        
        return triplets_sum_equals_zero