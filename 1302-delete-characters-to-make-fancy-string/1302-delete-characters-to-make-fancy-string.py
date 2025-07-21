class Solution:
    def makeFancyString(self, s: str) -> str:

        fancy_str = ''
        chars_freq_map = [0] * 26
        strt_idx = 0

        for end_idx in range(len(s)):
            curr_char = s[end_idx]
            chars_freq_map[ord(curr_char) - ord('a')] += 1
            window_size = end_idx - strt_idx + 1

            if window_size == 3:
                strt_char = s[strt_idx]

                if chars_freq_map[ord(strt_char) - ord('a')] < 3:
                    fancy_str += strt_char

                chars_freq_map[ord(strt_char) - ord('a')] -= 1
                strt_idx += 1
        
        while strt_idx < len(s):
            strt_char = s[strt_idx]

            if chars_freq_map[ord(strt_char) - ord('a')] < 3:
                fancy_str += strt_char

            chars_freq_map[ord(strt_char) - ord('a')] -= 1
            strt_idx += 1

        return fancy_str
        