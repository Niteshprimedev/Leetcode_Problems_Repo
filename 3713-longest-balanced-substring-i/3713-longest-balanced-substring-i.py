class Solution:
    def longestBalanced(self, s: str) -> int:
        '''
        def highestFreq(map):
            max_freq = 0

            for freq in map:
                max_freq = max(max_freq, freq)

            return max_freq
    
        right_map = [0] * 26

        for char in s:
            char_idx = ord(char) - ord('a')
            right_map[char_idx] += 1

        left_map = [0] * 26
        
        n = len(s)
        long_substr = 0
        strt = 0
        end = 0

        max_freq = 0

        while(end < n):
            end_idx = ord(s[end]) - ord('a')
            left_map[end_idx] += 1
            right_map[end_idx] -= 1

            while(right_map[end_idx] + left_map[end_idx] < highestFreq(left_map) and strt <= end):
                strt_idx = ord(s[strt]) - ord('a')
                
                left_map[strt_idx] -= 1
                
                strt += 1

            strt_idx = ord(s[strt]) - ord('a')
            while(right_map[strt_idx] + left_map[strt_idx] < highestFreq(left_map) and strt <= end):
                left_map[strt_idx] -= 1
                
                strt += 1
                strt_idx = ord(s[strt]) - ord('a')
                
            long_substr = max(long_substr, end - strt + 1)
            end += 1

        return long_substr
        '''

        long_substr = 1
        def isBalanced(list_map):
            frq_set = set()

            for val in list_map:
                if val > 0:
                    frq_set.add(val)

            return len(frq_set) == 1

        for i in range(len(s)):
            freq_map = [0] * 26
            
            for j in range(i, len(s)):
                c_idx = ord(s[j]) - ord('a')
                freq_map[c_idx] += 1

                if(isBalanced(freq_map)):
                    long_substr = max(long_substr, j - i + 1)

        return long_substr
            
        