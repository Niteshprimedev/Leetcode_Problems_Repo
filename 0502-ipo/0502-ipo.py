class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
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