class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        # Solution 1: Hint Solution and maintaining Two Min Heaps;
        start_min_heap = []
        end_min_heap = []

        n = len(costs)

        strt_idx = 0
        end_idx = n - 1
        total_hires = k
        total_cost = 0

        while total_hires > 0:
            
            while strt_idx <= end_idx and len(start_min_heap) < candidates:
                heapq.heappush(start_min_heap, costs[strt_idx])
                strt_idx += 1
            
            while end_idx >= strt_idx and len(end_min_heap) < candidates:
                heapq.heappush(end_min_heap, costs[end_idx])
                end_idx -= 1
            
            if start_min_heap and len(end_min_heap) == 0:
               total_cost += heapq.heappop(start_min_heap)
            elif end_min_heap and len(start_min_heap) == 0:
               total_cost += heapq.heappop(end_min_heap)
            elif start_min_heap and end_min_heap and start_min_heap[0] <= end_min_heap[0]:
                total_cost += heapq.heappop(start_min_heap)
            elif start_min_heap and end_min_heap and start_min_heap[0] >= end_min_heap[0]:
                total_cost += heapq.heappop(end_min_heap)

            total_hires -= 1
        
        return total_cost
        '''

        # Solution 2: Hint Solution and maintaining one Min Heap;
        min_heap = []

        n = len(costs)

        strt_idx = 0
        end_idx = n - 1
        total_hires = k
        total_cost = 0

        while strt_idx <= end_idx and strt_idx < candidates:
            encoded_val = costs[strt_idx] + strt_idx
            heapq.heappush(min_heap, (costs[strt_idx], strt_idx, 'start'))
            strt_idx += 1

        while end_idx >= strt_idx and end_idx >= (n - candidates):
            encoded_val = costs[end_idx] + end_idx
            heapq.heappush(min_heap, (costs[end_idx], end_idx, 'end'))
            end_idx -= 1


        while total_hires > 0:
            
            encoded_val, curr_idx, side = heapq.heappop(min_heap)

            cost = costs[curr_idx]
            total_cost += cost

            if side == 'start' and strt_idx <= end_idx:
                encoded_val = costs[strt_idx] + strt_idx
                heapq.heappush(min_heap, (costs[strt_idx], strt_idx, 'start'))
                strt_idx += 1
            elif end_idx >= strt_idx:
                encoded_val = costs[end_idx] + end_idx
                heapq.heappush(min_heap, (costs[end_idx], end_idx, 'end'))
                end_idx -= 1

            total_hires -= 1
        
        return total_cost
        