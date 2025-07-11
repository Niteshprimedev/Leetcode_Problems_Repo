class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        # Solution during Array Contest Week;
        # Problem No. 1
        nums = sorted(nums)
        triplets_sum_equals_zero = []

        for first_idx in range(len(nums)):
            first_num = nums[first_idx]
            # Skipping all the duplicates where first_num
            # is same as previous first_num value;
            if(first_idx > 0 and first_num == nums[first_idx - 1]):
                continue
            
            second_idx = first_idx + 1
            third_idx = len(nums) - 1

            while (second_idx < third_idx):
                second_num = nums[second_idx]
                third_num = nums[third_idx]

                triplets_sum = first_num + second_num + third_num

                if triplets_sum == 0:
                    triplets_sum_equals_zero.append([first_num, second_num, third_num])
                    second_idx +=1
                    third_idx -= 1

                    # Skipping all the duplicates where second_num
                    # is same as previous second_num value;
                    while second_idx < third_idx and nums[second_idx] == second_num:
                        second_idx += 1
                elif triplets_sum > 0:
                    third_idx -= 1
                else:
                    second_idx += 1
        
        return triplets_sum_equals_zero
        '''
            
        # Solution: Without using nested while loop;
        # The nested loop is important to have skip the duplicates
        # from the start but the third_num can also be repeating so need to skip
        # the second_num before checking for triplets_sum;
        # Problem No. 1
        nums = sorted(nums)
        triplets_sum_equals_zero = []

        for first_idx in range(len(nums)):
            first_num = nums[first_idx]
            # Skipping all the duplicates where first_num
            # is same as previous first_num value;
            if(first_idx > 0 and first_num == nums[first_idx - 1]):
                continue
            
            second_idx = first_idx + 1
            third_idx = len(nums) - 1

            while (second_idx < third_idx):
                second_num = nums[second_idx]
                third_num = nums[third_idx]

                triplets_sum = first_num + second_num + third_num

                if triplets_sum == 0:
                    triplets_sum_equals_zero.append([first_num, second_num, third_num])
                    second_idx +=1
                    third_idx -= 1

                    # Skipping all the duplicates where second_num
                    # is same as previous second_num value; cause the
                    # third num will also be repeating so it is important;
                    while second_idx < third_idx and nums[second_idx] == second_num:
                        second_idx += 1
                elif triplets_sum > 0:
                    third_idx -= 1
                else:
                    second_idx += 1
        
        return triplets_sum_equals_zero