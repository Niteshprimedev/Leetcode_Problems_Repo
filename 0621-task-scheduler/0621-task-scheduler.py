class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Logic: Use Hashmap to count the freq and then
        # create a max-heap of the freq + key, run while
        # until the max_heap exists and pop the first item
        # try to finish other tasks within the interval
        # and also wait for the given interval if no tasks
        # are left to finish to continue the same task again;

        import heapq
        chars_freq_arr = [0] * 26
        max_heap = []

        min_cpus_count = 0

        for task in tasks:
            char_idx = ord(task) - ord('A')

            chars_freq_arr[char_idx] += 1
        
        for idx_i in range(26):
            char_freq = chars_freq_arr[idx_i]
            if char_freq > 0:
                curr_char = chr(65 + idx_i)
                heapq.heappush(max_heap, (-char_freq, curr_char))

        # print(max_heap)

        while len(max_heap):
            first_task_freq, first_task = heapq.heappop(max_heap)
            first_task_freq = -first_task_freq

            idx_i = 0
            tasks_set = set()
            while idx_i < n and max_heap:
                task_freq, curr_task = heapq.heappop(max_heap)
                task_freq = -task_freq

                idx_i += 1

                if task_freq > 1:
                    tasks_set.add((-(task_freq - 1), curr_task))
            
            # print(tasks_set, first_task, idx_i)
            for curr_task in tasks_set:
                heapq.heappush(max_heap, curr_task)
            
            if first_task_freq > 1:
                heapq.heappush(max_heap, (-(first_task_freq - 1), first_task))

            if max_heap:
                min_cpus_count += (1 + n)
            else:
                min_cpus_count += idx_i + 1

        return min_cpus_count

        '''
        # Solution 2: Using Maths & Pure Maths;
        tasks_freq = [0] * 26
        max_count = 0

        for task in tasks:
            tasks_freq[ord(task) - ord('A')] += 1
            max_count = max(max_count, tasks_freq[ord(task) - ord('A')])

        time = (max_count - 1) * (n + 1)
        for f in tasks_freq:
            if f == max_count:
                time += 1
        
        return max(len(tasks), time)
        '''