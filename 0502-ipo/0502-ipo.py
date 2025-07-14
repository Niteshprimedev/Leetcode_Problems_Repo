class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        # Logic: Push all the profits which has the minimum capital
        # and then get the max profit, again push the profits for the
        # new minimum capital;

        pq = []
        cap_idx = 0
        total_projects = k
        total_capital = w

        sorted_capital = []

        for idx in range(len(profits)):
            sorted_capital.append([profits[idx], capital[idx]])
        
        sorted_capital.sort(key=lambda x:x[1])

        while total_projects > 0:
            while cap_idx < len(capital):
                curr_profit = sorted_capital[cap_idx][0]
                curr_capital = sorted_capital[cap_idx][1]

                if curr_capital <= total_capital:
                    heapq.heappush(pq, -curr_profit)
                    cap_idx += 1
                else:
                    break
            
            if len(pq) > 0:
                curr_profit = -heapq.heappop(pq)
                total_capital += curr_profit
            else:
                break

            total_projects -= 1

        return total_capital
        '''
        
        '''
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)

        return w
        '''

        n = len(profits)
        min_capital = [(capital[i], profits[i]) for i in range(n)]
        heapq.heapify(min_capital)

        maxProfit = []
        i = 0

        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)

        return w
