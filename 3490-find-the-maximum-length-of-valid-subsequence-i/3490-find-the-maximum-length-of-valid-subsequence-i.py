class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        # Observation:
        # Subsequences can either start with
        # (odd, odd), (odd, even), (even, odd), and (even, even)
        
        #  Edge Case:
        n = len(nums)
        if n < 2:
            return 0
        
        memo_dp = [[[-1 for _ in range(2)] for _ in range(n + 1)] for _ in range(n)]

        def all_valid_subs(prev_idx, curr_idx, parity_flag):
            # Base Case:
            if curr_idx == n:
                return 0
            
            if prev_idx != -1 and parity_flag != -1 and memo_dp[curr_idx][prev_idx][parity_flag] != -1:
                return memo_dp[curr_idx][prev_idx][parity_flag]

            pick_case = 0
            not_pick_case = 0

            if prev_idx == -1 or parity_flag == -1 or ((nums[prev_idx] + nums[curr_idx]) % 2 == parity_flag):
                new_parity_flag = parity_flag
                if prev_idx != -1:
                    # print(parity_flag, nums[prev_idx], nums[curr_idx])
                    new_parity_flag = (nums[prev_idx] + nums[curr_idx]) % 2
                    
                pick_case = 1 + all_valid_subs(curr_idx, curr_idx + 1, new_parity_flag)
            
            not_pick_case = all_valid_subs(prev_idx, curr_idx + 1, parity_flag)

            memo_dp[curr_idx][prev_idx][parity_flag] = max(pick_case, not_pick_case)
            return memo_dp[curr_idx][prev_idx][parity_flag]

        return all_valid_subs(-1, 0, -1)
        '''

        '''
        #  Edge Case:
        n = len(nums)
        if n < 2:
            return 0
        
        memo_dp = [[[0 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)]

        # Base Case:
        # for prev_idx in range(n - 1, -2, -1):
        #     for parity_flag in range(1, -2, -1):
        #         memo_dp[n][prev_idx + 1][parity_flag + 1] = 0

        for curr_idx in range(n - 1, -1, -1):
            for prev_idx in range(-1, curr_idx):
                for parity_flag in [-1, 0, 1]:

                    pick_case = 0
                    not_pick_case = 0

                    if prev_idx == -1 or parity_flag == -1 or ((nums[prev_idx] + nums[curr_idx]) % 2 == parity_flag):
                        new_parity_flag = parity_flag
                        if prev_idx != -1:
                            # print(parity_flag, nums[prev_idx], nums[curr_idx])
                            new_parity_flag = (nums[prev_idx] + nums[curr_idx]) % 2

                        pick_case = 1 + memo_dp[curr_idx + 1][curr_idx + 1][new_parity_flag + 1]
                    
                    not_pick_case = memo_dp[curr_idx + 1][prev_idx + 1][parity_flag + 1]

                    memo_dp[curr_idx][prev_idx + 1][parity_flag + 1] = max(pick_case, not_pick_case)

        return memo_dp[0][0][0]
        '''

        # Solution 3:
        # Observation based: Even, Odd, and Alternates;

        even_count = 0
        odd_count = 0
        alternate_count = 0
        parity_flag = -1

        for num in nums:
            # odd case, when last bit is set;
            if (num & 1) == 1:
                odd_count += 1

                if parity_flag == -1 or parity_flag == 0:
                    alternate_count += 1
            else:
                even_count += 1

                if parity_flag == -1 or parity_flag == 1:
                    alternate_count += 1
            
            parity_flag = num % 2

        return max(even_count, odd_count, alternate_count)
        