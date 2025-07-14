class Solution:
    def reorganizeString(self, s: str) -> str:
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
