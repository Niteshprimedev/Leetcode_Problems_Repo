class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Top Down Working Solution with Below Results;
        # TLE Without MemoDP
        # MLE with MemoDP:

        n = len(prices)
        memo_dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def all_days_buy_sell_profit(buy_idx, sell_idx):
            # Base Case:
            if buy_idx == n - 1 or sell_idx == n:
                return 0

            if memo_dp[buy_idx][sell_idx] != -1:
                return memo_dp[buy_idx][sell_idx]

            curr_price_sell_profit = 0
            if prices[buy_idx] < prices[sell_idx]:
                curr_price_sell_profit = prices[sell_idx] - prices[buy_idx] + all_days_buy_sell_profit(sell_idx + 1, sell_idx + 1)
            
            next_sell_price_profit = all_days_buy_sell_profit(buy_idx, sell_idx + 1)
            next_buy_price_profit = all_days_buy_sell_profit(buy_idx + 1, buy_idx + 1)

            memo_dp[buy_idx][sell_idx] = max(curr_price_sell_profit, next_sell_price_profit, next_buy_price_profit)
            return memo_dp[buy_idx][sell_idx]

        return all_days_buy_sell_profit(0, 0)
        '''

        # Logic:
        # Buying and then Selling
        # Top Down Approach Solution:
        
        total_days = len(prices)

        memo_dp = [[-1 for _ in range(2)] for _ in range(total_days)]

        def all_days_buy_sell_profit(curr_price_idx, buy_flag):
            # Base Case:
            if curr_price_idx == total_days:
                return 0 # You can't make any profit when there's no prices left;

            if memo_dp[curr_price_idx][buy_flag] != -1:
                return memo_dp[curr_price_idx][buy_flag]
        
            max_profit = 0

            # Buy Case:
            if(buy_flag == 1):
                # If you wanna buy then pay the current price;
                # And then you can sell;
                chose_to_buy = -prices[curr_price_idx] + all_days_buy_sell_profit(curr_price_idx + 1, 0)
                
                # If you don't wanna buy then no need to pay the current price;
                # And you are still searching for a better buying price so you can sell;
                # and maximize your profits
                skip_to_buy = all_days_buy_sell_profit(curr_price_idx + 1, 1)

                # max profit: for this buying & not buying decisions:
                max_profit = max(chose_to_buy, skip_to_buy)
            else:
                # If you wanna sell then get the current price as profit;
                # And now you can again buy;
                chose_to_sell = prices[curr_price_idx] + all_days_buy_sell_profit(curr_price_idx + 1, 1)
                
                # If you don't wanna sell then no price profit at current price;
                # And you are still searching for a better selling price so you can sell;
                # and maximize your profits
                skip_to_sell = all_days_buy_sell_profit(curr_price_idx + 1, 0)

                max_profit = max(chose_to_sell, skip_to_sell)

            memo_dp[curr_price_idx][buy_flag] = max_profit
            return memo_dp[curr_price_idx][buy_flag]

        return all_days_buy_sell_profit(0, 1)