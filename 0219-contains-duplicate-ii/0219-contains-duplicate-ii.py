class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        # Solution using Sliding Window and Hashmap
        # where we need the window size to be less than or equal to k;
        # and the two elements should be equal to each other;
        # nums[i] == nums[j] i.e x == y

        # Note: two distinct indices can't give abs diff as 0;
        if k == 0:
            return False

        window_strt_idx = 0
        nums_els_freq_map = {}
        is_contains_duplicate = False

        for window_end_idx in range(len(nums)):
            curr_el = nums[window_end_idx]

            nums_els_freq_map[curr_el] = nums_els_freq_map.get(curr_el, 0) + 1

            window_size = window_end_idx - window_strt_idx + 1

            while (window_size > k or window_end_idx == len(nums) - 1) and (window_strt_idx < window_end_idx + 1):
                # print(nums_els_freq_map)
                hash_value = nums_els_freq_map.get(nums[window_strt_idx], 0) - 1
                if hash_value == 0:
                    nums_els_freq_map.pop(nums[window_strt_idx], None) 
                elif hash_value >= 1:
                    is_contains_duplicate = True
                    break
                    nums_els_freq_map[nums[window_strt_idx]] = hash_value
                window_strt_idx += 1
                window_size = window_end_idx - window_strt_idx + 1

        return is_contains_duplicate
        '''

        # Sliding Window in set;
        is_contains_duplicate = False

        nums_els_set = set()

        for num_idx in range(len(nums)):
            curr_num = nums[num_idx]

            # if the duplicate is already present in set then found and stop
            if curr_num in nums_els_set:
                is_contains_duplicate = True
                break
            
            # if it is a new element and the set size is less than k window size;
            nums_els_set.add(curr_num)

            # if the set size is greater than or equal to k then remove the
            # old number at k - num_idx position ago
            if len(nums_els_set) > k:
                nums_els_set.remove(nums[num_idx - k])
            
        return is_contains_duplicate
