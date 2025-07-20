class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
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
        '''

        # Solution 3: Using Map and Merge_Sort;
        def merge(strt_idx, mid, end_idx, nums):
            merged_arr = []

            idx_i = strt_idx
            idx_j = mid + 1

            while idx_i <= mid and idx_j <= end_idx:
                if nums[idx_i] <= nums[idx_j]:
                    merged_arr.append(nums[idx_i])
                    idx_i += 1
                else:
                    merged_arr.append(nums[idx_j])
                    idx_j += 1
            
            while idx_i <= mid:
                merged_arr.append(nums[idx_i])
                idx_i += 1

            while idx_j <= end_idx:
                merged_arr.append(nums[idx_j])
                idx_j += 1

            for idx in range(len(merged_arr)):
                nums[idx + strt_idx] = merged_arr[idx]

            return nums

        def merge_sort(strt_idx, end_idx, nums):
            if strt_idx < end_idx:
                mid = strt_idx + (end_idx - strt_idx) // 2

                merge_sort(strt_idx, mid, nums)
                merge_sort(mid + 1, end_idx, nums)

                merge(strt_idx, mid, end_idx, nums)

            return nums
        
        n = len(nums)
        merge_sort(0, n - 1, nums)

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