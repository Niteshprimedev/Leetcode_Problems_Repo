class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1: using hashkeys and map;
        sorted_hashkey_group_value_map = {}

        for word in strs:
            hash_key = sorted(list(word))
            hash_key = ''.join(hash_key)

            if hash_key not in sorted_hashkey_group_value_map:
                sorted_hashkey_group_value_map[hash_key] = []
            
            sorted_hashkey_group_value_map[hash_key].append(word)
        
        return [value for hash_key, value in sorted_hashkey_group_value_map.items()]

        '''
        # Solution 2: using map and array;
        str_group_map = defaultdict(list)

        for curr_str in strs:
            chars_freq_arr = [0] * 26
            for char in curr_str:
                char_idx = ord(char) - ord('a')
                chars_freq_arr[char_idx] += 1
            
            str_group_map[tuple(chars_freq_arr)].append(curr_str)
        
        return list(str_group_map.values())
        '''

        