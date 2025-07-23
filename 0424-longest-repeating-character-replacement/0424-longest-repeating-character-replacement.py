class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Logic: Total Flips count,
        # simply create a window of longest size as
        # long as you can have at most k different chars 
        # replacements than the original char
        # Pre-Req - https://leetcode.com/problems/max-consecutive-ones-iii/description/
        
        # iDEA: To count the freq of all chars in my current window
        # and also count the max freq of a char, then replacements
        # are only possible for total_freq - max_freq <= k if it goes
        # greater than k then we can't replace and we need to shrink
        # Shrink the window as soon as total_freq - max_freq > k
        # Else expand the window as long as total_freq - max_freq <= k
        # replaced_chars = total_chars - max_char_freq
        # Maintaining a window is fine but finding the max_freq
        # is looping through the loop again and again for 26 chars

        longest_substr_len = 0
        max_char_freq = 0
        window_strt_idx = 0
        chars_arr_map = [0] * 26

        def calculate_max_freq(strt_idx, end_idx, chars_map):
            total_chars = end_idx - strt_idx + 1
            max_freq = 0

            # Loop at most 26 times;
            if total_chars < 26:
                for strt_idx in range(end_idx + 1):
                    curr_char = s[strt_idx]
                    char_idx = ord(curr_char) - ord('A')
                    max_freq = max(chars_map[char_idx], max_freq)
            else:
                for idx in range(26):
                    max_freq = max(chars_map[idx], max_freq)
            
            return max_freq

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]
            char_idx = ord(curr_char) - ord('A')

            # Expand the window to replace more chars;
            chars_arr_map[char_idx] += 1

            max_char_freq = max(max_char_freq, chars_arr_map[char_idx])
            total_chars = window_end_idx - window_strt_idx + 1
            replaced_chars = total_chars - max_char_freq

            # Shrink the window as replaced_chars count is reached
            if replaced_chars > k:
                strt_char = s[window_strt_idx]
                strt_char_idx = ord(strt_char) - ord('A')

                chars_arr_map[strt_char_idx] -= 1
                window_strt_idx += 1
                
                # count the next max freq of the window chars
                max_char_freq = calculate_max_freq(window_strt_idx, window_end_idx, chars_arr_map)
            
            # Update the longest substring length
            window_size = window_end_idx - window_strt_idx + 1
            longest_substr_len = max(longest_substr_len, window_size)
        
        return longest_substr_len

        # Solution 2: Striver Bhaiya Reference
        # Removed the helper function to calculate the max_char_freq
        # of the current window char;

        longest_substr_len = 0
        max_char_freq = 0
        window_strt_idx = 0
        chars_arr_map = [0] * 26

        # def calculate_max_freq(strt_idx, end_idx, chars_map):
        #     total_chars = end_idx - strt_idx + 1
        #     max_freq = 0

        #     # Loop at most 26 times;
        #     if total_chars < 26:
        #         for strt_idx in range(end_idx + 1):
        #             curr_char = s[strt_idx]
        #             char_idx = ord(curr_char) - ord('A')
        #             max_freq = max(chars_map[char_idx], max_freq)
        #     else:
        #         for idx in range(26):
        #             max_freq = max(chars_map[idx], max_freq)
            
        #     return max_freq

        for window_end_idx in range(len(s)):
            curr_char = s[window_end_idx]
            char_idx = ord(curr_char) - ord('A')

            # Expand the window to replace more chars;
            chars_arr_map[char_idx] += 1

            max_char_freq = max(max_char_freq, chars_arr_map[char_idx])
            total_chars = window_end_idx - window_strt_idx + 1
            replaced_chars = total_chars - max_char_freq

            # Shrink the window as replaced_chars count is reached
            if replaced_chars > k:
                strt_char = s[window_strt_idx]
                strt_char_idx = ord(strt_char) - ord('A')

                chars_arr_map[strt_char_idx] -= 1
                window_strt_idx += 1
                
                # count the next max freq of the window chars
                # max_char_freq = calculate_max_freq(window_strt_idx, window_end_idx, chars_arr_map)
            
            # Update the longest substring length
            window_size = window_end_idx - window_strt_idx + 1
            longest_substr_len = max(longest_substr_len, window_size)
        
        return longest_substr_len
