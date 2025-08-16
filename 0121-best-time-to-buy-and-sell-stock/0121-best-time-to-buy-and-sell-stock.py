class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
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
        '''

        '''
        # solution using monotonic stack:

        monotonic_stack = []
        max_profit = 0

        for price_idx in range(len(prices)):
            price = prices[price_idx]
            buy_price = prices[price_idx]

            new_max_profit = 0

            if len(monotonic_stack) == 0:
                monotonic_stack.append(price_idx)

            prev_buy_price = prices[monotonic_stack[0]]

            if prev_buy_price < buy_price:
                new_max_profit = price - prev_buy_price
            else:
                new_max_profit = price - buy_price
                monotonic_stack[0] = price_idx
                
            max_profit = max(max_profit, new_max_profit)

        return max_profit
        '''

        # Solution2: Calculate the max_stock_price seen so far
        # and the curr_buy_price is where you can maximize the profit;

        total_days = len(prices)
        last_day_price_idx = total_days - 1

        max_stock_sell_price = prices[last_day_price_idx]
        max_stock_buy_sell_profit = 0

        for price_idx in range(total_days - 1, -1, -1):
            curr_stock_buy_price = prices[price_idx]
            new_max_stock_sell_price = curr_stock_buy_price

            max_stock_sell_price = max(max_stock_sell_price, new_max_stock_sell_price)
            new_max_stock_buy_sell_profit = max_stock_sell_price - curr_stock_buy_price

            max_stock_buy_sell_profit = max(max_stock_buy_sell_profit, new_max_stock_buy_sell_profit)
        
        return max_stock_buy_sell_profit