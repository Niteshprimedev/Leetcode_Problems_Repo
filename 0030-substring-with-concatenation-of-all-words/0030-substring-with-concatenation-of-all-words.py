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

        # create a freq map of the words arr
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

        # start checking the substrings till last char before the total_words_size
        while window_end_idx < loop_len:
            idx = window_end_idx
            words_arr = []

            # run a loop until the total_words_size from curr_idx
            while idx < (window_end_idx + total_words_size):
                curr_word = s[idx: idx + word_size]
                
                # and check each word of word_size length to be in map
                if curr_word in words_map:

                    # if the word in map, this is potential a part of substring
                    curr_word = s[idx: idx + word_size]
                    words_arr.append(curr_word)
                # else break the loop
                else:
                    break     

                idx += word_size          

            # if the words_arr has same number of words then check freq;
            if len(words_arr) == len(words):
                if frequency_map(words_arr) == words_map:
                    concatenated_strings.append(window_end_idx)

            # continue checking with the next char;
            window_end_idx += 1
        
        return concatenated_strings


        # barfoothefoobarman
        # barfoo, arfoot, foothe, thefoo, foobar, barman
        # bar, foo => freq (1, 1) => matched => pushed hence 0 ans
        # arf => not in map break, not same length go to next char check
        # foo (in), the not in map => break, not same length
        # the => not in map break
        # foo, bar => freq (1, 1) => matches => pushed & next hence 9 ans
        # bar, man (not in map), break and done with iteration;