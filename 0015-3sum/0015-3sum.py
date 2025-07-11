class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        unique_triplets_list = []

        # Using 3 Sum Logic here;
        for second_idx in range(n):
            second_num = nums[second_idx]

            if second_idx > 0 and second_num == nums[second_idx - 1]:
                continue
            
            third_idx = second_idx + 1
            forth_idx = n - 1

            while third_idx < forth_idx:
                third_num = nums[third_idx]
                forth_num = nums[forth_idx]

                triplets_sum = second_num + third_num + forth_num
                # print(triplets_sum, third_idx)

                if triplets_sum == 0:
                    unique_triplets_list.append([second_num, third_num, forth_num])
                    third_idx += 1
                    forth_idx -= 1

                    while third_idx < forth_idx and nums[third_idx] == third_num:
                        third_idx += 1
                
                elif triplets_sum < 0:
                    third_idx += 1
                elif triplets_sum > 0: 
                    forth_idx -= 1
        
        return unique_triplets_list
        