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

        # Solution 3: Using Map and Merge_Sort;
        def merge(strt_idx, mid, end_idx, str_arr):
            merged_arr = []

            idx_i = strt_idx
            idx_j = mid + 1

            while idx_i <= mid and idx_j <= end_idx:
                if ord(str_arr[idx_i]) <= ord(str_arr[idx_j]):
                    merged_arr.append(str_arr[idx_i])
                    idx_i += 1
                else:
                    merged_arr.append(str_arr[idx_j])
                    idx_j += 1
            
            while idx_i <= mid:
                merged_arr.append(str_arr[idx_i])
                idx_i += 1

            while idx_j <= end_idx:
                merged_arr.append(str_arr[idx_j])
                idx_j += 1

            for idx in range(len(merged_arr)):
                str_arr[idx + strt_idx] = merged_arr[idx]

            return str_arr

        def merge_sort(strt_idx, end_idx, str_arr):
            if strt_idx < end_idx:
                mid = strt_idx + (end_idx - strt_idx) // 2

                merge_sort(strt_idx, mid, str_arr)
                merge_sort(mid + 1, end_idx, str_arr)

                merge(strt_idx, mid, end_idx, str_arr)

            return str_arr
        
        str_group_map = defaultdict(list)

        for curr_str in strs:
            sorted_str = merge_sort(0, len(curr_str) - 1, list(curr_str))

            str_group_map[tuple(sorted_str)].append(curr_str) 

        return [values for hash_key, values in sorted_hashkey_group_value_map.items()]

        