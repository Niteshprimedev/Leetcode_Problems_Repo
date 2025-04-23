class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Note: Buy & Sell = 1 Transaction
        # 
        total_days = len(prices)

        memo_dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(total_days)]

        def all_days_buy_sell_profits(curr_price_idx, buy_flag, transactions_count):
            # Base Case:
            if curr_price_idx == total_days:
                return 0

            if memo_dp[curr_price_idx][buy_flag][transactions_count] != -1:
                return memo_dp[curr_price_idx][buy_flag][transactions_count]
            
            max_profits = 0

            if(buy_flag == 1):
                chose_to_buy = -prices[curr_price_idx] + all_days_buy_sell_profits(curr_price_idx + 1, 0, transactions_count)
                skip_to_buy = all_days_buy_sell_profits(curr_price_idx + 1, 1, transactions_count)

                max_profits = max(chose_to_buy, skip_to_buy)
            elif(transactions_count < 2):
                chose_to_sell = prices[curr_price_idx] + all_days_buy_sell_profits(curr_price_idx + 1, 1, transactions_count + 1)
                skip_to_sell = all_days_buy_sell_profits(curr_price_idx + 1, 0, transactions_count)

                max_profits = max(chose_to_sell, skip_to_sell)

            # print(buy_flag, transactions_count)
            memo_dp[curr_price_idx][buy_flag][transactions_count] = max_profits
            return memo_dp[curr_price_idx][buy_flag][transactions_count]

        return all_days_buy_sell_profits(0, 1, 0)
    '''

        # Bottom Up Approach:
        total_days = len(prices)

        memo_dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(total_days + 1)]

        # Base Cases:
        # for curr_idx in range(total_days - 1, -1, -1):
        for buy_flag in range(1, -1, -1):
            for transactions_count in range(2, -1, -1):
                memo_dp[total_days][buy_flag][transactions_count] = 0


        # For loops:
        for curr_price_idx in range(total_days - 1, -1, -1):
            for buy_flag in range(1, -1, -1):
                for transactions_count in range(2, -1, -1):
                    max_profits = 0

                    if(buy_flag == 1):
                        chose_to_buy = -prices[curr_price_idx] + memo_dp[curr_price_idx + 1][0][transactions_count]
                        skip_to_buy = memo_dp[curr_price_idx + 1][1][transactions_count]

                        max_profits = max(chose_to_buy, skip_to_buy)
                    elif(transactions_count < 2):
                        chose_to_sell = prices[curr_price_idx] + memo_dp[curr_price_idx + 1][1][transactions_count + 1]
                        skip_to_sell = memo_dp[curr_price_idx + 1][0][transactions_count]

                        max_profits = max(chose_to_sell, skip_to_sell)

                    # print(buy_flag, transactions_count)
                    memo_dp[curr_price_idx][buy_flag][transactions_count] = max_profits
        
        return memo_dp[0][1][0]

