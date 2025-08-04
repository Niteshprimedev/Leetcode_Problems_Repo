class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        # Another way to say this is: 
        # Find the maximum subarray with at most 2 different fruits.

        # Observation: you only have two baskets: meaning you only can 
        # pick two type of fruits at max. And any number of fruits are allowe
        # Note: if basket 1 has fruit type = 3 then it can only have 3 fruit type 
        # and if basket 2 has fruit type = 4 then it can only have 4 fruit type

        # Logic: to create a window with 2 types of fruits only and reset the window
        # whenever a third type of fruit is encountered;
        # const fruitTypesMap = new Map();

        max_fruits_picked = 0
        window_strt_idx = 0
        fruit_types_map = {}

        for window_end_idx in range(len(fruits)):
            curr_fruit_type = fruits[window_end_idx]

            if curr_fruit_type not in fruit_types_map:
                fruit_types_map[curr_fruit_type] = 0
            
            fruit_types_map[curr_fruit_type] += 1

            while len(fruit_types_map) > 2 and window_strt_idx < window_end_idx + 1:
                strt_fruit_type = fruits[window_strt_idx]

                fruit_types_map[strt_fruit_type] -= 1

                if fruit_types_map[strt_fruit_type] == 0:
                    fruit_types_map.pop(strt_fruit_type, None)

                window_strt_idx += 1
            
            new_max_fruits_picked = window_end_idx - window_strt_idx + 1
            max_fruits_picked = max(max_fruits_picked, new_max_fruits_picked)

        return max_fruits_picked
        '''

        # Another way to say this is: 
        # Find the maximum subarray with at most 2 different fruits.

        # Solution2: Optimal Solution by Removing Nested Loop;
        max_fruits_picked = 0
        window_strt_idx = 0
        fruit_types_map = {}

        for window_end_idx in range(len(fruits)):
            curr_fruit_type = fruits[window_end_idx]

            if curr_fruit_type not in fruit_types_map:
                fruit_types_map[curr_fruit_type] = 0
            
            fruit_types_map[curr_fruit_type] += 1

            if len(fruit_types_map) > 2:
                strt_fruit_type = fruits[window_strt_idx]

                fruit_types_map[strt_fruit_type] -= 1

                if fruit_types_map[strt_fruit_type] == 0:
                    fruit_types_map.pop(strt_fruit_type, None)

                window_strt_idx += 1
            else:
                new_max_fruits_picked = window_end_idx - window_strt_idx + 1
                max_fruits_picked = max(max_fruits_picked, new_max_fruits_picked)

        return max_fruits_picked
