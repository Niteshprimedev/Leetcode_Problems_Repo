class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        # Greedy and sorting;

        # Sorty by start time first and then by end time
        # if two events have same start time;
        events.sort(key=lambda x:(x[0], x[1])) #sort by start

        print(events)
        total_events = 0
        curr_day = 1
        for start_time, end_time in events:
            if start_time <= curr_day and end_time >= curr_day:
                curr_day += 1
                total_events += 1
        
        return total_events
        '''

        '''
        # Solution 1
        # Valid Solution after seeing solution:

        # sort the events based on start time;
        events.sort()

        total_events = 0

        max_end_day = 10**5 + 1
        event_idx = 0
        n = len(events)

        pq = [] # for min_heap to get earliest end day;

        for day in range(1, max_end_day):
            
            # Add events that start on this day
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(pq, events[event_idx][1])
                event_idx += 1
            
            if pq:
                # Attend the event that ends earliest today;
                heapq.heappop(pq)
                total_events += 1

            # Remove the events that are ended;
            while pq and pq[0] <= day:
                heapq.heappop(pq)

            # break if no more events are left;
            if event_idx == n and len(pq) == 0:
                break
        
        return total_events
        '''
        
        # Solution 2: Remove events that are ended
        # sort the events based on start time;
        events.sort()

        total_events = 0

        max_end_day = 10**5 + 1
        event_idx = 0
        n = len(events)

        pq = [] # for min_heap to get earliest end day;

        for day in range(1, max_end_day):
            # Remove the events that are ended;
            while pq and pq[0] < day:
                heapq.heappop(pq)
            
            # Add events that start on this day
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(pq, events[event_idx][1])
                event_idx += 1
            
            if pq:
                # Attend the event that ends earliest today;
                heapq.heappop(pq)
                total_events += 1


            # break if no more events are left;
            if event_idx == n and len(pq) == 0:
                break
        
        return total_events