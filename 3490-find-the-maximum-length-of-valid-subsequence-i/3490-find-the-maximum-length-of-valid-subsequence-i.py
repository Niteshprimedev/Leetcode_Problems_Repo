class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        # Observation: TLE with TOP DOWN
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
        '''

        '''
        # Solution 4:
        # Observation Even, odd, and alterantes;

        patterns = [[0,0], [1,1], [0,1], [1, 0]]
        max_subs_len = 0

        for pattern in patterns:
            # count is basically gives 0 & 1 when % with 2
            # so we check the pattern at count = 0 or 1
            curr_max_subs = 0
            
            for num in nums:
                idx = curr_max_subs % 2
                # Here we check for [0, 0]
                # Here we check for [0, 1]
                # Here we check for [1, 1]
                # Here we check for [1, 0] 
                # 0th index and then 1st index using the count;
                # this way we ensure the parities are all even
                # all odd or alternates;
                if num % 2 == pattern[idx]:
                    curr_max_subs += 1
        
            max_subs_len = max(max_subs_len, curr_max_subs)
        
        return max_subs_len
        '''

        '''
        # Solution 5:
        # Observation Even, odd, and alterantes;
        n = len(nums)
        patterns = [[0,0], [1,1], [0,1], [1, 0]]
        max_subs_len = 0

        def count_subs_with_pattern(curr_idx, need_idx, parity_states):
            if curr_idx == n:
                return 0

            if memo_dp[curr_idx][need_idx] != -1:
                return memo_dp[curr_idx][need_idx]

            # Pick case
            pick_case = 0

            if (nums[curr_idx] % 2) == parity_states[need_idx]:
                new_need_idx = 1 if need_idx == 0 else 0 #alternate b/w 1 and 0 indices;
                pick_case = 1 + count_subs_with_pattern(curr_idx + 1, new_need_idx, parity_states)
            
            # Skip case
            not_pick_case = count_subs_with_pattern(curr_idx + 1, need_idx, parity_states)

            memo_dp[curr_idx][need_idx] = max(pick_case, not_pick_case)
            return max(pick_case, not_pick_case)

        for parity_states in patterns:
            memo_dp = [[-1 for _ in range(2)] for _ in range(n)]
            new_max_subs_len = count_subs_with_pattern(0, 0, parity_states)
            max_subs_len = max(max_subs_len, new_max_subs_len)
        
        return max_subs_len
        '''
        
        # Solution 6:
        # Observation Even, odd, and alterantes;
        # Using alternate parities which is more readable;

        n = len(nums)
        patterns = [[0,0], [1,1], [0,1], [1, 0]]
        max_subs_len = 0

        def count_subs_with_pattern(curr_idx, need_idx, first_parity, second_parity):
            if curr_idx == n:
                return 0

            if memo_dp[curr_idx][need_idx] != -1:
                return memo_dp[curr_idx][need_idx]

            # Pick case
            pick_case = 0

            if (nums[curr_idx] % 2) == first_parity:
                pick_case = 1 + count_subs_with_pattern(curr_idx + 1, need_idx, second_parity, first_parity)
            
            # Skip case
            not_pick_case = count_subs_with_pattern(curr_idx + 1, need_idx, first_parity, second_parity)

            memo_dp[curr_idx][need_idx] = max(pick_case, not_pick_case)
            return max(pick_case, not_pick_case)

        for parity_states in patterns:
            first_parity = parity_states[0]
            second_parity = parity_states[1]

            memo_dp = [[-1 for _ in range(2)] for _ in range(n)]
            new_max_subs_len = count_subs_with_pattern(0, 0, first_parity, second_parity)
            max_subs_len = max(max_subs_len, new_max_subs_len)
        
        return max_subs_len

        