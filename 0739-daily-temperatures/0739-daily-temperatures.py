class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        # During DSA Session 8 on May 25:
        # Logic: Next Greater Element & Stack

        arr_len = len(temperatures)

        daily_temps = [0] * arr_len
        next_greater_stack = []

        for idx_i in range(arr_len - 1, -1, -1):
            curr_temp = temperatures[idx_i]

            while next_greater_stack and temperatures[next_greater_stack[-1]] <= curr_temp:
                next_greater_stack.pop()
            
            if next_greater_stack:
                next_idx = next_greater_stack[-1]
                daily_temps[idx_i] = next_idx - idx_i
            else:
                daily_temps[idx_i] = 0
            
            next_greater_stack.append(idx_i)
        
        return daily_temps
        '''

        # Solution 2: Updating the If Conditions for daily_temps;
        arr_len = len(temperatures)

        daily_temps = [0] * arr_len
        next_greater_stack = []

        for idx_i in range(arr_len - 1, -1, -1):
            curr_temp = temperatures[idx_i]

            while next_greater_stack and temperatures[next_greater_stack[-1]] <= curr_temp:
                next_greater_stack.pop()
            
            # there's no warmer temperature throughout my temp days
            warmer_temp_day = 0

            # or calculate the number of days where I got warmer temperature 
            if next_greater_stack:
                # the number of days need to wait to get the warmer temperature
                next_idx = next_greater_stack[-1]
                warmer_temp_day = next_idx - idx_i

            daily_temps[idx_i] = warmer_temp_day
            
            next_greater_stack.append(idx_i)
        
        return daily_temps
