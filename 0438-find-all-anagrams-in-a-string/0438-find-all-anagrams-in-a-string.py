class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        def isAnagrams(map1, map2):
            for i in range(26):
                if map1[i] != map2[i]:
                    return False
            
            return True

        str_s_map = [0] * 26
        str_t_map = [0] * 26

        for char in p:
            char_idx = ord(char) - ord('a')
            str_t_map[char_idx] += 1

        n = len(s)
        strt_idx = 0
        end_idx = 0

        anagrams_res = []

        while(end_idx < n):
            char_idx = ord(s[end_idx]) - ord('a')
            str_s_map[char_idx] += 1

            if(end_idx - strt_idx + 1 == len(p)):
                if isAnagrams(str_s_map, str_t_map):
                    anagrams_res.append(strt_idx)

                char_idx = ord(s[strt_idx]) - ord('a')
                str_s_map[char_idx] -= 1

                strt_idx += 1

            end_idx += 1
        
        return anagrams_res
        '''

        '''
        # Logic: Using minimum window substring idea;

        anagrams_res = []
        str_t_chars_map = [0] * 26

        for char in p:
            char_idx = ord(char) - ord('a')
            str_t_chars_map[char_idx] += 1

        n = len(s)
        strt_idx = 0
        end_idx = 0
        total_matches = 0

        while(end_idx < n):
            char_idx = ord(s[end_idx]) - ord('a')
            str_t_chars_map[char_idx] -= 1

            if(str_t_chars_map[char_idx] >= 0):
                total_matches += 1

            if(end_idx - strt_idx + 1 == len(p)):
                if total_matches == len(p):
                    anagrams_res.append(strt_idx)

                char_idx = ord(s[strt_idx]) - ord('a')
                str_t_chars_map[char_idx] += 1

                if(str_t_chars_map[char_idx] > 0):
                    total_matches -= 1

                strt_idx += 1

            end_idx += 1

        return anagrams_res
        ''' 

        # Meta Prep Time Practice:

        anagrams_res = []

        # freq map of pattern 'p'
        # stores how many of each char we NEED
        freq = [0] * 26

        for char in p:
            freq[ord(char) - ord('a')] += 1

        n = len(s)
        left = 0
        right = 0

        # counts how many characters are MATCHED so far
        total_matches = 0

        """
        🧠 CORE IDEA:

        freq[] = "how many chars we still need"

        → When we include a char:
            freq[c]--

            if freq[c] >= 0 → it was needed → match++

        → When we remove a char:
            freq[c]++

            if freq[c] > 0 → we lost a needed char → match--
        """

        while right < n:

            # include current char in window
            idx = ord(s[right]) - ord('a')
            freq[idx] -= 1

            # if it was needed → we matched one char
            if freq[idx] >= 0:
                total_matches += 1

            """
            🧠 When window size == len(p):

            We check:
            → did we match ALL chars of p?
            → total_matches == len(p)
            """

            if right - left + 1 == len(p):

                # valid anagram found
                if total_matches == len(p):
                    anagrams_res.append(left)

                # remove left char (slide window)
                left_idx = ord(s[left]) - ord('a')
                freq[left_idx] += 1

                # if this char was contributing → we lose match
                if freq[left_idx] > 0:
                    total_matches -= 1

                left += 1

            right += 1

        return anagrams_res