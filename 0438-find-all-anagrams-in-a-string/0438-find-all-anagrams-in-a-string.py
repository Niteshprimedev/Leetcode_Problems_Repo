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





        