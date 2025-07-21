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
        '''

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
        '''

        # Solution 4: Using Map and Quick_sort;
        # Pivot as low or start element;
        def partition(low, high, nums):
            pivot_el = nums[low]

            # temp swap the pivot with high val
            nums[low], nums[high] = nums[high], nums[low]

            idx_i = low - 1

            for idx_j in range(low, high):
                if nums[idx_j] <= pivot_el:
                    idx_i += 1
                    nums[idx_i], nums[idx_j] = nums[idx_j], nums[idx_i]
                
            idx_i += 1
            nums[idx_i], nums[high] = nums[high], nums[idx_i]

            return idx_i

        def quick_sort(low, high, nums):
            if low < high:
                pivot_idx = partition(low, high, nums)

                quick_sort(low, pivot_idx - 1, nums)
                quick_sort(pivot_idx + 1, high, nums)

            return nums
        
        n = len(nums)
        quick_sort(0, n - 1, nums)

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