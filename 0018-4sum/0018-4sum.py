class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Solution: O(N^3)
        # [2,2,2,2,2,2,2,2,2]
        # first = 0, second = 1
        # third = 2 & forth = 8
        # valid quads => 0, 1, 2, & 8
        # incrementing and decrementing the pointers;
        # and then skipping all the duplicate values;
        n = len(nums)
        nums.sort()

        unique_quadruples_list = []

        for first_idx in range(n):
            first_num = nums[first_idx]
            if first_idx > 0 and first_num == nums[first_idx - 1]:
                continue
            
            # Using 3 Sum Logic here;
            for second_idx in range(first_idx + 1, n):
                second_num = nums[second_idx]

                if second_idx > (first_idx + 1) and second_num == nums[second_idx - 1]:
                    continue
                
                third_idx = second_idx + 1
                forth_idx = n - 1

                while third_idx < forth_idx:
                    third_num = nums[third_idx]
                    forth_num = nums[forth_idx]

                    quadruplets_sum = first_num + second_num + third_num + forth_num
                    # print(quadruplets_sum, third_idx)

                    if quadruplets_sum == target:
                        unique_quadruples_list.append([first_num, second_num, third_num, forth_num])
                        third_idx += 1
                        forth_idx -= 1

                        while third_idx < forth_idx and nums[third_idx] == third_num:
                            third_idx += 1
                    
                    elif quadruplets_sum < target:
                        third_idx += 1
                    elif quadruplets_sum > target: 
                        forth_idx -= 1
        
        return unique_quadruples_list

