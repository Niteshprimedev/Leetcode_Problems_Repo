class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        # code here
        # Binary Search Solution:
        # Intuition:
        # While traversing we try to create multiple 
        # LIS forms and then later on figure out the max one
        # But instead of tracking the multiple instances
        # of LIS, we can overwrite the existing LIS whenever 
        # we find any element which is smaller than the last element
        # in our current LIS
        # This way, we ensure the length of longest increasing subsequence
        # Note: we overwrite the currEl with our existing element in LIS
        # at the position where the element is found or at the next greater
        # element position; 
        
        def binary_search_idx(sorted_arr, target):
            left_idx = 0
            right_idx = len(sorted_arr) - 1
            
            while(left_idx < right_idx):
                middle_idx = left_idx + (right_idx - left_idx) // 2
                
                if sorted_arr[middle_idx] >= target:
                    right_idx = middle_idx
                else:
                    left_idx = middle_idx + 1
                    
            return left_idx
        
        longest_els_len = []
        longest_inc_subseq_len = 1
        
        longest_els_len.append(nums[0])
        
        for curr_idx in range(1, len(nums)):
            last_idx = len(longest_els_len) - 1
            
            if nums[curr_idx] > longest_els_len[last_idx]:
                longest_els_len.append(nums[curr_idx])
                longest_inc_subseq_len += 1
            else:
                # Binary Search: 
                # If the element exists then it's index
                # else the index of the next greater element;
                found_idx = binary_search_idx(longest_els_len, nums[curr_idx])
                longest_els_len[found_idx] = nums[curr_idx]
        
        return longest_inc_subseq_len
        '''

        '''
        # Solution 2:
        # Top Down Solution: TLE in Python

        if len(nums) == 1:
            return 1

        n = len(nums)
        memo_dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def all_inc_subseq(curr_idx, next_el_idx):
            # Base Case:
            if curr_idx == 0:
                if next_el_idx < n and nums[curr_idx] < nums[next_el_idx]:
                    return 1
                else:
                    return 0
            
            if memo_dp[curr_idx][next_el_idx] != -1:
                return memo_dp[curr_idx][next_el_idx]
            
            pick_case = 0
            if next_el_idx == n or nums[curr_idx] < nums[next_el_idx]:
                pick_case = 1 + all_inc_subseq(curr_idx - 1, curr_idx)

            not_pick_case = 0 + all_inc_subseq(curr_idx - 1, next_el_idx)

            memo_dp[curr_idx][next_el_idx] = max(pick_case, not_pick_case)
            return memo_dp[curr_idx][next_el_idx]

        return all_inc_subseq(n - 1, n)
        '''

        '''
        # Solution 3: Bottom Up Approach;
        if len(nums) == 1:
            return 1

        n = len(nums)
        memo_dp = [[0 for _ in range(n + 1)] for _ in range(n)]

        # Base Case:
        for next_el_idx in range(1, n + 1):
            if next_el_idx < n and nums[0] < nums[next_el_idx]:
                memo_dp[0][next_el_idx] = 1
            else:
                memo_dp[0][next_el_idx] = 0
        
        for curr_idx in range(1, n):
            for next_el_idx in range(curr_idx + 1, n + 1):
                pick_case = 0

                if next_el_idx == n or (nums[curr_idx] < nums[next_el_idx]):
                    pick_case = 1 + memo_dp[curr_idx - 1][curr_idx]
                
                not_pick_case = 0 + memo_dp[curr_idx - 1][next_el_idx]

                memo_dp[curr_idx][next_el_idx] = max(pick_case, not_pick_case)

        return memo_dp[n - 1][n]
        '''

        # Solution 4: Space Optimized Bottom Up Approach;
        if len(nums) == 1:
            return 1

        n = len(nums)
        prev_dp = [0 for _ in range(n + 1)]

        # Base Case:
        for next_el_idx in range(1, n + 1):
            if next_el_idx < n and nums[0] < nums[next_el_idx]:
                prev_dp[next_el_idx] = 1
            else:
                prev_dp[next_el_idx] = 0
        
        for curr_idx in range(1, n):
            curr_dp = [0 for _ in range(n + 1)]
            for next_el_idx in range(curr_idx + 1, n + 1):
                pick_case = 0

                if next_el_idx == n or (nums[curr_idx] < nums[next_el_idx]):
                    pick_case = 1 + prev_dp[curr_idx]
                
                not_pick_case = 0 + prev_dp[next_el_idx]

                curr_dp[next_el_idx] = max(pick_case, not_pick_case)

            prev_dp = curr_dp

        return prev_dp[n]