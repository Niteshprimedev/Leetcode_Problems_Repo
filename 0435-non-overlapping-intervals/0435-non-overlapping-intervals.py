class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Logic: Sort the intervals based on end_time
        # and then remove the overlapping intervals

        intervals.sort(key=lambda x:x[1])

        min_intervals_count = 0
        prev_interval = intervals[0]

        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            # Is interval overlapping?
            if prev_interval[1] > interval[0]:
                min_intervals_count += 1
            else:
                prev_interval = interval
    
        return min_intervals_count

        