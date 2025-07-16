class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        # Top Down: Memoization Approach gives TLE
        n = len(nums)
        # Edge Case:
        if n == 1:
            return 1

        memo_dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def all_inc_subsequences(curr_idx, prev_idx):
            # Base Case:
            if curr_idx == (n - 1):
                if nums[curr_idx] > nums[prev_idx]:
                    return 1
                else:
                    return 0
            
            if memo_dp[curr_idx][prev_idx + 1] != -1:
                return memo_dp[curr_idx][prev_idx + 1]

            # Pick Case:
            pick_case = 0
            if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
                pick_case = 1 + all_inc_subsequences(curr_idx + 1, curr_idx)

            # Not Pick Case
            not_pick_case = 0 + all_inc_subsequences(curr_idx + 1, prev_idx)

            memo_dp[curr_idx][prev_idx + 1] = max(pick_case, not_pick_case)
            # print(memo_dp)
            return memo_dp[curr_idx][prev_idx + 1]
        
        return all_inc_subsequences(0, -1)
        '''
        
        # Bottom Up: Tabulation Approach 
        n = len(nums)
        # Edge Case:
        if n == 1:
            return 1

        memo_dp = [[0 for _ in range(n + 1)] for _ in range(n)]

        # Base Case:
        for prev_idx in range(n - 2, -2, -1):
            if prev_idx == -1 or nums[n - 1] > nums[prev_idx]:
                memo_dp[n - 1][prev_idx + 1] = 1
        
        for curr_idx in range(n - 2, -1, -1):
            for prev_idx in range(curr_idx - 1, -2, -1):
                # Pick Case:
                pick_case = 0
                if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
                    pick_case = 1 + memo_dp[curr_idx + 1][curr_idx + 1]

                # Not Pick Case
                not_pick_case = 0 + memo_dp[curr_idx + 1][prev_idx + 1]

                memo_dp[curr_idx][prev_idx + 1] = max(pick_case, not_pick_case)
                # print(memo_dp)
        
        # print(memo_dp)
        return memo_dp[0][0]
