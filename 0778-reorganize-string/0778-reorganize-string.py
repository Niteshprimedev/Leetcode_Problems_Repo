class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        # Solution using Max Heap and chars frequency logic;
        str_chars_freq_hash_map = collections.Counter(s)

        max_heap = [(-freq, char) for char, freq in str_chars_freq_hash_map.items()]

        heapq.heapify(max_heap)

        # print('after', max_heap)
        reorganized_str_list = []

        while len(max_heap) >= 2:
            top_freq, top_char = heapq.heappop(max_heap)
            next_freq, next_char = heapq.heappop(max_heap)

            reorganized_str_list.append(top_char)
            reorganized_str_list.append(next_char)

            if top_freq + 1:
                heapq.heappush(max_heap, (top_freq + 1, top_char))

            if next_freq + 1:
                heapq.heappush(max_heap, (next_freq + 1, next_char))

        if max_heap:
            top_freq, top_char = heapq.heappop(max_heap)

            print(reorganized_str_list, top_freq, top_char)
            if top_freq != -1 or (len(reorganized_str_list) > 1 and top_char == reorganized_str_list[-1]):
                return ''
            else:
                reorganized_str_list.append(top_char)
        
        return "".join(reorganized_str_list)
        '''
        
        '''
        # GFG Time Solution:
        str_chars_freq_map = collections.Counter(s)
    
        max_heap = [(-freq, char) for char, freq in str_chars_freq_map.items()]
        
        heapq.heapify(max_heap)
        
        rearrange_str_list = []
        
        while len(max_heap) >= 2:
            top_freq, top_char = heapq.heappop(max_heap)
            next_freq, next_char = heapq.heappop(max_heap)
            
            rearrange_str_list.append(top_char)
            rearrange_str_list.append(next_char)
            
            if top_freq + 1 < 0:
                heapq.heappush(max_heap, (top_freq + 1, top_char))
            if next_freq + 1 < 0:
                heapq.heappush(max_heap, (next_freq + 1, next_char))
        
        if len(max_heap) > 0:
            top_freq, top_char = heapq.heappop(max_heap)
            
            if top_freq != -1 or (len(rearrange_str_list) > 1 and rearrange_str_list[-1] == top_char):
                return ''
            else:
                rearrange_str_list.append(top_char)
            
        return ''.join(rearrange_str_list)
        '''

        max_heap = []

        reorganized_str = ''

        chars_freq_map = [0] * 26

        for char in s:
            char_idx = ord(char) - ord('a')
            chars_freq_map[char_idx] += 1
        
        for idx in range(26):
            if chars_freq_map[idx] > 0:
                char_freq = -1 * chars_freq_map[idx]
                char = chr(idx + 97)
                heapq.heappush(max_heap, (char_freq, char))

        while len(max_heap) >= 2:
            first_char_freq, first_char = heapq.heappop(max_heap)
            second_char_freq, second_char = heapq.heappop(max_heap)

            reorganized_str += first_char + second_char

            if (-1 * first_char_freq) > 1:
                heapq.heappush(max_heap, (first_char_freq + 1, first_char))
            if (-1 * second_char_freq) > 1:
                heapq.heappush(max_heap, (second_char_freq + 1, second_char))
        
        if max_heap:
            # print(max_heap[0][0], reorganized_str[-1])
            if max_heap[0][0] != -1 or reorganized_str != '' and reorganized_str[-1] == max_heap[0][1]:
                return ''
            else:
                reorganized_str += max_heap[0][1]
        
        return reorganized_str
