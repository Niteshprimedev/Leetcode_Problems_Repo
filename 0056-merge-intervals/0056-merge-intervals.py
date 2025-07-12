class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        # Solution 1: Using the stack pop and push for 
        # last interval;

        merged_intervals = []
        # sort the intervals based on the first val
        intervals.sort(key=lambda x:x[0])

        merged_intervals.append(intervals[0])

        for idx_i in range(1, len(intervals)):
            curr_interval = intervals[idx_i]
            merge_interval = merged_intervals.pop()

            if curr_interval[0] <= merge_interval[1]:
                merge_interval[1] = max(merge_interval[1], curr_interval[1])
                merged_intervals.append(merge_interval)
            else:
                merged_intervals.append(merge_interval)
                merged_intervals.append(curr_interval)
        
        return merged_intervals
        '''

        # Solution 2: Minimum Operations on array;
        intervals.sort(key=lambda x:x[0])

        merged_intervals = []

        prev_interval = intervals[0]

        for idx_i in range(1, len(intervals)):
            curr_interval = intervals[idx_i]

            if prev_interval[1] >= curr_interval[0]:
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
            else:
                merged_intervals.append(prev_interval)
                prev_interval = curr_interval
            
        merged_intervals.append(prev_interval)

        return merged_intervals