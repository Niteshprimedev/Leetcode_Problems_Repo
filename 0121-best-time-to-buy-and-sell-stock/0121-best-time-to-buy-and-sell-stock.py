class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Top Down Approach Solution:
        total_days = len(prices)

        memo_dp = [[-1 for _ in range(2)] for _ in range(total_days)]

        def all_days_buy_sell_profits(curr_price_idx, buy_flag):
            # Base Case:
            if curr_price_idx == total_days or buy_flag == -1:
                return 0
            
            if memo_dp[curr_price_idx][buy_flag] != -1:
                return memo_dp[curr_price_idx][buy_flag]
            
            max_profit = 0
            # Buying Case:
            if (buy_flag == 1):
                chose_to_buy = -prices[curr_price_idx] + all_days_buy_sell_profits(curr_price_idx + 1, 0)

                skip_to_buy = all_days_buy_sell_profits(curr_price_idx + 1, 1)

                max_profit = max(chose_to_buy, skip_to_buy)
            
            elif (buy_flag == 0):
                chose_to_sell = prices[curr_price_idx] + all_days_buy_sell_profits(curr_price_idx + 1, -1)

                skip_to_sell = all_days_buy_sell_profits(curr_price_idx + 1, 0)

                max_profit = max(chose_to_sell, skip_to_sell)
            
            memo_dp[curr_price_idx][buy_flag] = max_profit
            return memo_dp[curr_price_idx][buy_flag]

        return all_days_buy_sell_profits(0, 1)