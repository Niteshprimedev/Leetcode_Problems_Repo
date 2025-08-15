class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        # TLE Solution;
        words_map = defaultdict(int)

        for word in words:
            words_map[word] += 1
        
        concatenated_strings = []
        word_size = len(words[0])

        window_end_idx = 0
        total_words_size = word_size * len(words)
        loop_len = len(s) - total_words_size + 1
        total_matches = 0

        while window_end_idx < loop_len:
            idx = window_end_idx

            while idx < (window_end_idx + total_words_size):
                curr_word = s[idx: idx + word_size]

                if curr_word in words_map and words_map[curr_word] - 1 >= 0:
                    words_map[curr_word] -= 1
                    total_matches += 1
                else:
                    break               

                idx += word_size
            
            # if window_end_idx == 13:
            #     print(total_matches, len(words), words_map, idx)

            if total_matches == len(words):
                concatenated_strings.append(window_end_idx)
            
            idx = window_end_idx
            while idx < (window_end_idx + total_words_size):
                curr_word = s[idx: idx + word_size]

                if curr_word in words_map and total_matches > 0:
                    words_map[curr_word] += 1
                    total_matches -= 1
                else:
                    break               

                idx += word_size

            window_end_idx += 1
        
        return concatenated_strings
        '''

        def frequency_map(word_list):
            freq = defaultdict(int)

            for word in word_list:
                freq[word] += 1
            
            return freq

        words_map = frequency_map(words)
        
        concatenated_strings = []
        word_size = len(words[0])

        total_words_size = word_size * len(words)
        loop_len = len(s) - total_words_size + 1

        window_end_idx = 0
        while window_end_idx < loop_len:
            idx = window_end_idx
            words_arr = []

            while idx < (window_end_idx + total_words_size):
                curr_word = s[idx: idx + word_size]
                if curr_word in words_map:
                    curr_word = s[idx: idx + word_size]
                    words_arr.append(curr_word)
                else:
                    break     

                idx += word_size          

            if len(words_arr) == len(words):
                if frequency_map(words_arr) == words_map:
                    concatenated_strings.append(window_end_idx)

            window_end_idx += 1
        
        return concatenated_strings