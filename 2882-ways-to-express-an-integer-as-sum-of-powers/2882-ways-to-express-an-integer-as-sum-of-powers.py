class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        total_ways = 0

        memo_dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def allPowers(curr_num, curr_sum):
            # Base Case:
            if curr_sum == 0:
                return 1
            elif curr_num > n or curr_sum < 0:
                return 0

            if memo_dp[curr_num][curr_sum] != -1:
                return memo_dp[curr_num][curr_sum]

            # pick case:
            pick_case = 0
            not_pick_case = 0

            curr_pow = curr_num ** x

            if(curr_pow <= curr_sum):
                pick_case = allPowers(curr_num + 1, curr_sum - curr_pow)
            
                not_pick_case = allPowers(curr_num + 1, curr_sum)

            memo_dp[curr_num][curr_sum] = (pick_case + not_pick_case) % MOD
            return memo_dp[curr_num][curr_sum]

        return allPowers(1, n)
