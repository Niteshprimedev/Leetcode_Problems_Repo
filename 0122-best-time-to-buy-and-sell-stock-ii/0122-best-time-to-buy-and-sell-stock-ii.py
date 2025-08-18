class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        '''

        '''
        # Bottom Up Approach Solution:
        total_days = len(prices)

        memo_dp = [[-1 for _ in range(2)] for _ in range(total_days + 1)]

        # Base Case:
        for buy_flag in range(2):
            memo_dp[total_days][buy_flag] = 0
        
        # for loops:
        for curr_price_idx in range(total_days - 1, -1, -1):
            for buy_flag in range(1, -1, -1):
                max_profit = 0

                # Buy Case:
                if(buy_flag == 1):
                    # If you wanna buy then pay the current price;
                    # And then you can sell;
                    chose_to_buy = -prices[curr_price_idx] + memo_dp[curr_price_idx + 1][0]
                    
                    # If you don't wanna buy then no need to pay the current price;
                    # And you are still searching for a better buying price so you can sell;
                    # and maximize your profits
                    skip_to_buy = memo_dp[curr_price_idx + 1][1]

                    # max profit: for this buying & not buying decisions:
                    max_profit = max(chose_to_buy, skip_to_buy)
                else:
                    # If you wanna sell then get the current price as profit;
                    # And now you can again buy;
                    chose_to_sell = prices[curr_price_idx] + memo_dp[curr_price_idx + 1][1]
                    
                    # If you don't wanna sell then no price profit at current price;
                    # And you are still searching for a better selling price so you can sell;
                    # and maximize your profits
                    skip_to_sell = memo_dp[curr_price_idx + 1][0]

                    max_profit = max(chose_to_sell, skip_to_sell)

                memo_dp[curr_price_idx][buy_flag] = max_profit
            
        return memo_dp[0][1]
        '''

        # Space Optimized Bottom Up Approach Solution::
        total_days = len(prices)

        prev_dp = [-1 for _ in range(2)]

        # Base Case:
        for buy_flag in range(2):
            prev_dp[buy_flag] = 0
        
        # for loops:
        for curr_price_idx in range(total_days - 1, -1, -1):
            curr_dp = [-1 for _ in range(2)]
            for buy_flag in range(1, -1, -1):
                max_profit = 0

                # Buy Case:
                if(buy_flag == 1):
                    # If you wanna buy then pay the current price;
                    # And then you can sell;
                    chose_to_buy = -prices[curr_price_idx] + prev_dp[0]
                    
                    # If you don't wanna buy then no need to pay the current price;
                    # And you are still searching for a better buying price so you can sell;
                    # and maximize your profits
                    skip_to_buy = prev_dp[1]

                    # max profit: for this buying & not buying decisions:
                    max_profit = max(chose_to_buy, skip_to_buy)
                else:
                    # If you wanna sell then get the current price as profit;
                    # And now you can again buy;
                    chose_to_sell = prices[curr_price_idx] + prev_dp[1]
                    
                    # If you don't wanna sell then no price profit at current price;
                    # And you are still searching for a better selling price so you can sell;
                    # and maximize your profits
                    skip_to_sell = prev_dp[0]

                    max_profit = max(chose_to_sell, skip_to_sell)

                curr_dp[buy_flag] = max_profit
            
            prev_dp = curr_dp
            
        return prev_dp[1]

        '''
        # Space Optimized Variables Optional Bottom Up Approach Solution:
        total_days = len(prices)

        # Base Case:
        ahead_not_buy = 0
        ahead_buy = 0
        
        # for loops:
        for curr_price_idx in range(total_days - 1, -1, -1):

            # If you wanna buy then pay the current price;
            # And then you can sell;
            chose_to_buy = -prices[curr_price_idx] + ahead_not_buy
            
            # If you don't wanna buy then no need to pay the current price;
            # And you are still searching for a better buying price so you can sell;
            # and maximize your profits
            skip_to_buy = ahead_buy

            # max profit: for this buying & not buying decisions:
            # Buy Case:
            curr_buy = max(chose_to_buy, skip_to_buy)
            
            # If you wanna sell then get the current price as profit;
            # And now you can again buy;
            chose_to_sell = prices[curr_price_idx] + ahead_buy
            
            # If you don't wanna sell then no price profit at current price;
            # And you are still searching for a better selling price so you can sell;
            # and maximize your profits
            skip_to_sell = ahead_not_buy

            curr_not_buy = max(chose_to_sell, skip_to_sell)

            ahead_buy = curr_buy
            ahead_not_buy = curr_not_buy
            
        return ahead_buy
        '''

        '''
        # Space Optimized Variables Optional Bottom Up Approach Solution:
        # with buy_flag and above is without buy_flag;
        total_days = len(prices)

        # Base Case:
        ahead_not_buy = 0
        ahead_buy = 0
        
        # for loops:
        for curr_price_idx in range(total_days - 1, -1, -1):
            for buy_flag in range(2):
                # Buy Case:
                if(buy_flag == 1):
                    # If you wanna buy then pay the current price;
                    # And then you can sell;
                    chose_to_buy = -prices[curr_price_idx] + ahead_not_buy
                    
                    # If you don't wanna buy then no need to pay the current price;
                    # And you are still searching for a better buying price so you can sell;
                    # and maximize your profits
                    skip_to_buy = ahead_buy

                    # max profit: for this buying & not buying decisions:
                    ahead_buy = max(chose_to_buy, skip_to_buy)
                else:
                    # If you wanna sell then get the current price as profit;
                    # And now you can again buy;
                    chose_to_sell = prices[curr_price_idx] + ahead_buy
                    
                    # If you don't wanna sell then no price profit at current price;
                    # And you are still searching for a better selling price so you can sell;
                    # and maximize your profits
                    skip_to_sell = ahead_not_buy

                    ahead_not_buy = max(chose_to_sell, skip_to_sell)
        
        return ahead_buy
        '''

        '''
        # Peek and Valley Solution:

        max_profit = 0
        price_idx = 0

        while price_idx < len(prices):
            buy_price = prices[price_idx]
            price_idx += 1

            while price_idx < len(prices) and buy_price >= prices[price_idx]:
                buy_price = prices[price_idx]
                price_idx += 1
            
            if price_idx == len(prices):
                break
                
            sell_price = prices[price_idx]
            price_idx += 1

            while price_idx < len(prices) and sell_price <= prices[price_idx]:
                sell_price = prices[price_idx]
                price_idx += 1
            
            max_profit += sell_price - buy_price
        
        return max_profit
        '''