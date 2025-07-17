class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        '''
        n = len(nums)
        memo_dp = [[[-1 for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(n)]

        def all_valid_subs(curr_idx, next_idx, parity_flag):
            # Base Case:
            if curr_idx < 0:
                return 0
            
            if memo_dp[curr_idx][next_idx][parity_flag] != -1:
                return memo_dp[curr_idx][next_idx][parity_flag]
            
            # Pick Case
            pick_case = 0

            # print(curr_idx, next_idx, parity_flag)
            if next_idx == n or parity_flag == -1 or ((nums[curr_idx] + nums[next_idx]) % k == parity_flag):
                new_parity_flag = parity_flag
                if next_idx < n:
                    new_parity_flag = (nums[curr_idx] + nums[next_idx]) % k
                pick_case = 1 + all_valid_subs(curr_idx - 1, curr_idx, new_parity_flag)

            # Not Pick Case
            not_pick_case = 0 + all_valid_subs(curr_idx - 1, next_idx, parity_flag)

            memo_dp[curr_idx][next_idx][parity_flag] = max(pick_case, not_pick_case)
            return memo_dp[curr_idx][next_idx][parity_flag]

        return all_valid_subs(n - 1, n, -1)
        '''

        '''
        # Solution 2: Similar to Version 1 but TLE;
        n = len(nums)
        memo_dp = [[-1 for _ in range(k + 1)] for _ in range(n)]
        max_subs_len = 0

        def count_subs_with_rem(curr_idx, prev_rem, remainder_i):
            # Base Case:
            if curr_idx == n:
                return 0
            
            memo_col = prev_rem + 1
            if memo_dp[curr_idx][memo_col] != -1:
                return memo_dp[curr_idx][memo_col]
            
            # Pick Case
            pick_case = 0
            
            curr_rem = nums[curr_idx] % k

            if prev_rem == -1 or ((curr_rem + prev_rem) % k == remainder_i):
                pick_case = 1 + count_subs_with_rem(curr_idx + 1, curr_rem, remainder_i)

            # Not Pick Case
            not_pick_case = 0 + count_subs_with_rem(curr_idx + 1, prev_rem, remainder_i)

            memo_dp[curr_idx][memo_col] = max(pick_case, not_pick_case)
            return memo_dp[curr_idx][memo_col]         

        # cause initially for previous version we had
        # 0 and 1 parities only so (0 - 2)
        # but in this k version we can have
        # remainders as (0, 1, 2, 3, all upto k - 1) so loop till k;
        for remainder_i in range(k):
            memo_dp = [[-1 for _ in range(k + 1)] for _ in range(n)]
            new_max_subs_len = count_subs_with_rem(0, -1, remainder_i)
            max_subs_len = max(max_subs_len, new_max_subs_len)
        
        return max_subs_len
        '''
        
        '''
        # Solution 3: Bottom Up of Previous Version 1;
        
        # cause initially for previous version we had
        # 0 and 1 parities only so (0 - 2)
        # but in this k version we can have
        # remainders as (0, 1, 2, 3, all upto k - 1) so loop till k;

        n = len(nums)
        max_subs_len = 0

        for remainder_i in range(k):
            memo_dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

            # No Base Case cause dp is already 0;
            for curr_idx in range(n - 1, -1, -1):
                for prev_rem in range(k - 1, -2, -1):
                    memo_col = prev_rem + 1

                    # Pick Case
                    pick_case = 0
                    
                    curr_rem = nums[curr_idx] % k

                    if prev_rem == -1 or ((curr_rem + prev_rem) % k == remainder_i):
                        pick_case = 1 + memo_dp[curr_idx + 1][curr_rem + 1]

                    # Not Pick Case
                    not_pick_case = 0 + memo_dp[curr_idx + 1][memo_col]

                    memo_dp[curr_idx][memo_col] = max(pick_case, not_pick_case)

            new_max_subs_len = memo_dp[0][0]
            max_subs_len = max(max_subs_len, new_max_subs_len)
        
        return max_subs_len
        '''

        # Solution 4: Bottom Up 1D;
        
        n = len(nums)
        max_subs_len = 0

        for remainder_i in range(k):
            memo_dp = [0 for _ in range(k)]

            for num in nums:
                curr_rem = num % k
                prev_rem = (remainder_i - curr_rem) % k

                memo_dp[curr_rem] = max(memo_dp[curr_rem], memo_dp[prev_rem] + 1)

                new_max_subs_len = memo_dp[curr_rem]
                max_subs_len = max(max_subs_len, new_max_subs_len)
        
        return max_subs_len

