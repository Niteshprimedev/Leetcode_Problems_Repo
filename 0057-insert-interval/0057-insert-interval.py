class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Binary Search and Merging;

        n = len(intervals)
        def binary_search(interval, intervals):
            target = interval[0]

            left = 0
            right = n - 1
            insertion_idx = -1

            while left <= right:
                mid = left + (right - left) // 2

                if intervals[mid][0] > target:
                    right = mid - 1
                else:
                    insertion_idx = mid
                    left = mid + 1
            
            intervals = intervals[:insertion_idx + 1] + [newInterval] + intervals[insertion_idx + 1:]
            return intervals

        intervals = binary_search(newInterval, intervals)

        merged_intervals = []
        prev_interval = intervals[0]

        # print(intervals)

        for idx in range(1, n + 1):
            curr_interval = intervals[idx]

            if prev_interval[1] >= curr_interval[0]:
                # print(prev_interval)
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
            else:
                merged_intervals.append(prev_interval)
                prev_interval = curr_interval
        
        # print(prev_interval)
        merged_intervals.append(prev_interval)

        return merged_intervals        