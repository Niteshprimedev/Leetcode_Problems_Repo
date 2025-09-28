class Solution:
    def fib(self, n: int) -> int:
        '''
        # Recursive Solution: Solved during DSA Session 15 on June 21

        def compute_fib(n):
            # Base Case:
            if n == 0 or n == 1:
                return n
            
            return compute_fib(n - 1) + compute_fib(n - 2)
        
        return compute_fib(n)
        '''

        '''
        # Top Down Solution: Solved during DSA Session 15 on June 21
        memo_dp = [-1 for _ in range(n + 1)]

        def compute_fib(n):
            # Base Case:
            if n == 0 or n == 1:
                memo_dp[n] = n
                return n
            
            if memo_dp[n] != -1:
                return memo_dp[n]

            memo_dp[n] = compute_fib(n - 1) + compute_fib(n - 2)
            return memo_dp[n]
        
        compute_fib(n)

        # print(memo_dp)

        return memo_dp[n]
        '''

        '''
        # Bottom Up Solution: Solved during DSA Session 15 on June 21
        if n == 0 or n == 1:
            return n

        memo_dp = [-1 for _ in range(n + 1)]

        # Base Case:
        memo_dp[0] = 0
        memo_dp[1] = 1

        for idx_i in range(2, n + 1):
            memo_dp[idx_i] = memo_dp[idx_i - 1] + memo_dp[idx_i - 2]
        
        return memo_dp[n]
        '''

        # Space Optimized Bottom Up Solution: 
        # Solved during DSA Session 15 on June 21
        if n == 0 or n == 1:
            return n

        # Base Case:
        second_num = 0
        first_num = 1

        for idx_i in range(2, n + 1):
            curr_num = first_num + second_num
            second_num = first_num
            first_num = curr_num
        
        return first_num