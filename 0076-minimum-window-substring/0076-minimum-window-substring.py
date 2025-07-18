class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        # Solution 1: using hashmap;
        # Hats off to this Striver Bhaiyaaaa:
        # The solution worked like anything :)
        
        min_window_substr = ''
        min_window_substr_len = len(s) + 1

        str_t_chars_map = {}

        for char in t:
            str_t_chars_map[char] = str_t_chars_map.get(char, 0) + 1

        total_matching_chars_count = 0
        window_strt_idx = 0

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]

            hash_value = str_t_chars_map.get(curr_char, 0)
            # if curr_char in str_t_chars_map:
            #     if hash_value > 0:
            #         total_matching_chars_count += 1
            #     hash_value -= 1
                
            #     str_t_chars_map[curr_char] = hash_value
            # else:
            #     str_t_chars_map[curr_char] = hash_value - 1
            if hash_value > 0:
                total_matching_chars_count += 1
                
            str_t_chars_map[curr_char] = hash_value - 1
            
            while total_matching_chars_count == len(t) and window_strt_idx < window_end_idx + 1:
                window_size = window_end_idx - window_strt_idx + 1

                if window_size < min_window_substr_len:
                    min_window_substr_len = window_size
                    min_window_substr = s[window_strt_idx:window_end_idx + 1]
                
                strt_char = s[window_strt_idx]
                hash_value = str_t_chars_map.get(strt_char) + 1

                if hash_value > 0:
                    total_matching_chars_count -= 1
                
                str_t_chars_map[strt_char] = hash_value
                window_strt_idx += 1

        return min_window_substr
        '''

        # Solution 2: using array hashmap;
        # Hats off to this Striver Bhaiyaaaa:
        # The solution worked like anything :)
        
        min_window_substr = ''
        min_window_substr_len = len(s) + 1

        str_t_chars_map = [0] * 256

        for char in t:
            char_idx = ord(char)
            str_t_chars_map[char_idx] += 1

        total_matching_chars_count = 0
        window_strt_idx = 0

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]
            char_idx = ord(curr_char)

            hash_value = str_t_chars_map[char_idx]
            if hash_value > 0:
                total_matching_chars_count += 1
                
            str_t_chars_map[char_idx] = hash_value - 1
            
            while total_matching_chars_count == len(t) and window_strt_idx < window_end_idx + 1:
                window_size = window_end_idx - window_strt_idx + 1

                if window_size < min_window_substr_len:
                    min_window_substr_len = window_size
                    min_window_substr = s[window_strt_idx:window_end_idx + 1]
                
                strt_char = s[window_strt_idx]
                strt_char_idx = ord(strt_char)
                hash_value = str_t_chars_map[strt_char_idx] + 1

                if hash_value > 0:
                    total_matching_chars_count -= 1
                
                str_t_chars_map[strt_char_idx] = hash_value
                window_strt_idx += 1

        return min_window_substr
