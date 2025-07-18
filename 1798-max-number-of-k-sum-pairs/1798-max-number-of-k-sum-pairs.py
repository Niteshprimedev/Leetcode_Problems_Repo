class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        # Logic: Sort the nums array using built-in or sorting algos
        # and then use two pointers technique to find k-sum pairs;

        # Solution using Merge Sort Algo;
        n = len(nums)

        def merge_arrays(strt, mid, end, nums):
            merged_arr = []

            idx_i = strt
            idx_j = mid + 1

            while idx_i <= mid and idx_j <= end:
                if nums[idx_i] <= nums[idx_j]:
                    merged_arr.append(nums[idx_i])
                    idx_i += 1
                else:
                    merged_arr.append(nums[idx_j])
                    idx_j += 1
            
            while idx_i <= mid:
                merged_arr.append(nums[idx_i])
                idx_i += 1

            while idx_j <= end:
                merged_arr.append(nums[idx_j])
                idx_j += 1
            
            for idx in range(len(merged_arr)):
                nums[idx + strt] = merged_arr[idx]
            
            return nums

        def merge_sort(strt, end, nums):
            if strt < end:
                mid = strt + (end - strt) // 2

                merge_sort(strt, mid, nums)
                merge_sort(mid + 1, end, nums)

                merge_arrays(strt, mid, end, nums)
                return nums
            
            return nums
        
        merge_sort(0, n - 1, nums)

        # print(nums)

        strt_idx = 0
        end_idx = n - 1
        max_pairs_count = 0

        while strt_idx < end_idx:
            curr_sum = nums[strt_idx]  + nums[end_idx]

            if curr_sum == k:
                max_pairs_count += 1
                strt_idx += 1
                end_idx -= 1
            elif curr_sum > k:
                end_idx -= 1
            else:
                strt_idx += 1

        return max_pairs_count
        '''
        
        # Solution 2 using Built in Sort;
        n = len(nums)

        nums.sort()
        # print(nums)

        strt_idx = 0
        end_idx = n - 1
        max_pairs_count = 0

        while strt_idx < end_idx:
            curr_sum = nums[strt_idx]  + nums[end_idx]

            if curr_sum == k:
                max_pairs_count += 1
                strt_idx += 1
                end_idx -= 1
            elif curr_sum > k:
                end_idx -= 1
            else:
                strt_idx += 1

        return max_pairs_count

        '''
        # Solution 3: Using Hashmap and No Sorting;
        # Just need to count unique pairs equal k-sum;
        max_pairs_count = 0

        right_side_els_map = defaultdict(int)

        for num in nums:
            right_side_els_map[num] += 1
        
        for first_num in nums:
            right_side_els_map[first_num] -= 1

            second_num = k - first_num

            if right_side_els_map[second_num] > 0 and right_side_els_map[first_num] >= 0:
                max_pairs_count += 1
                right_side_els_map[second_num] -= 1
        
        return max_pairs_count
        '''
        
        '''
        # Solution 4: Using Hashmap and No Sorting;
        # Just need to count unique pairs equal k-sum;
        # Only Pass Solution
        max_pairs_count = 0

        nums_els_map = defaultdict(int)

        for first_num in nums:
            second_num = k - first_num

            if nums_els_map[second_num] > 0:
                max_pairs_count += 1
                nums_els_map[second_num] -= 1
            else:
                nums_els_map[first_num] += 1
        
        return max_pairs_count
        '''





