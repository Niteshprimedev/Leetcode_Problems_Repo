class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Solution using Hash set and Sliding Window:

        window_strt_idx = 0
        unique_chars_map = {}

        longest_substr_len = 0

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]

            if curr_char in unique_chars_map:
                # deleting chars till the repeated char range cause window reset;
                hash_value = unique_chars_map.get(curr_char, 0) 
                while window_strt_idx < hash_value:
                    unique_chars_map.pop(s[window_strt_idx], None)
                    window_strt_idx += 1
                
                window_strt_idx = hash_value + 1

            # if longest_substr_len > 10:
                # print(window_strt_idx, window_end_idx)
                # print(s[window_strt_idx], s[window_end_idx])

            unique_chars_map[curr_char] = window_end_idx
            window_size = window_end_idx - window_strt_idx + 1
            longest_substr_len = max(longest_substr_len, window_size)
            # print(unique_chars_map)

            # Or length of unique characters in map;
            # total_unique_chars = len(unique_chars_map)
            # longest_substr_len = max(longest_substr_len, total_unique_chars)

        return longest_substr_len
        '''

        '''
        # Solution using Hash set and Sliding Window:
        # Optimized: Avoid deleting all the chars in hashmap;

        window_strt_idx = 0
        unique_chars_map = {}

        longest_substr_len = 0

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]

            if curr_char in unique_chars_map:
                hash_value = unique_chars_map.get(curr_char, 0) 

                # so even the curr_char is present in map
                # but is it having a valid index or is it in my
                # sliding window range between start and end?
                # if yes then, move strt_idx else just update the new occurence later
                if hash_value + 1 > window_strt_idx:                
                    window_strt_idx = hash_value + 1

            unique_chars_map[curr_char] = window_end_idx
            window_size = window_end_idx - window_strt_idx + 1
            longest_substr_len = max(longest_substr_len, window_size)
            # print(unique_chars_map)

            # Or length of unique characters in map;
            # total_unique_chars = len(unique_chars_map)
            # longest_substr_len = max(longest_substr_len, total_unique_chars)

        return longest_substr_len
        '''

        # Solution using Array Map and Sliding Window:
        # Optimized: Avoid deleting all the chars in hashmap;

        window_strt_idx = 0
        unique_chars_arr = [-1] * 256

        longest_substr_len = 0

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]
            char_ascii_val = ord(curr_char)

            if unique_chars_arr[char_ascii_val] != -1:
                hash_value = unique_chars_arr[char_ascii_val] 

                # so even the curr_char is present in map
                # but is it having a valid index or is it in my
                # sliding window range between start and end?
                # if yes then, move strt_idx else just update the new occurence later
                if hash_value + 1 > window_strt_idx:                
                    window_strt_idx = hash_value + 1

            unique_chars_arr[char_ascii_val] = window_end_idx
            window_size = window_end_idx - window_strt_idx + 1
            longest_substr_len = max(longest_substr_len, window_size)
            # print(unique_chars_arr)

            # Or length of unique characters in map;
            # total_unique_chars = len(unique_chars_arr)
            # longest_substr_len = max(longest_substr_len, total_unique_chars)

        return longest_substr_len