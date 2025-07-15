class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueDS:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, new_node):
        if self.rear != None:
            self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front == None:
            return None
        temp = self.front
        self.front = self.front.next

        return temp.val

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        # Login: maintain a queue with max value at the front
        # minimum value at the rear end;

        # Solution1 : Using Shradhaa Ma'am Logic & it is 
        # based on Queue Data structure + sliding Window pattern;

        queue = []
        sliding_window_maxms = []

        for idx_i in range(k):
            curr_num = nums[idx_i]

            while queue and nums[queue[-1]] <= curr_num:
                queue.pop()

            queue.append(idx_i)   
        
        sliding_window_maxms.append(nums[queue[0]])

        for idx_i in range(k, len(nums)):
            curr_num = nums[idx_i]

            while queue and nums[queue[-1]] <= curr_num:
                queue.pop()
            
            while queue and (idx_i - queue[0]) >= k:
                queue.pop(0)
            
            queue.append(idx_i)
            sliding_window_maxms.append(nums[queue[0]])

        return sliding_window_maxms
        '''
       
        '''
        # Login: maintain a queue with max value at the front
        # minimum value at the rear end;

        # Solution2 : Using Shradhaa Ma'am Logic & it is 
        # based on Priority Queue Max Heap Data structure + sliding Window pattern;
        # Since python in-built heap DS is a Min-Heap so use -negative values to 
        # make it a Max-Heap Data Structure;
        # Updated Code: Removed the unnecessary variables prev_num and prev_idx
        # cause they are not used anywhere;

        import heapq

        priority_q = []
        sliding_window_maxms = []

        for idx_i in range(k):
            curr_num = nums[idx_i]

            heapq.heappush(priority_q, (-curr_num, idx_i))  
        
        sliding_window_maxms.append(-priority_q[0][0])
        # print(priority_q)

        for idx_i in range(k, len(nums)):
            curr_num = nums[idx_i]

            # only pop items from the heap when the window becomes invalid;
            while priority_q and (idx_i - priority_q[0][1]) >= k:
                heapq.heappop(priority_q)
            
            heapq.heappush(priority_q, (-curr_num, idx_i))  
            sliding_window_maxms.append(-priority_q[0][0])

        return sliding_window_maxms
        '''

        # Solution 3: Doing the TO-DO; The while loop takes care of 
        # any elements that goes beyond our window so the pq can't have
        # more than k elements;
        # @TO-DO: The Priority Queue currently has more than k elements
        # and this is not required, since our window only needs max
        # of k elements so need to optimize my data storage in PQ;

        # Logic: maintain a queue with max value at the front
        # minimum value at the rear end;

        import heapq

        priority_q = []
        sliding_window_maxms = []

        for idx_i in range(k):
            curr_num = nums[idx_i]

            heapq.heappush(priority_q, (-curr_num, idx_i))  
        
        sliding_window_maxms.append(-priority_q[0][0])
        # print(priority_q)

        for idx_i in range(k, len(nums)):
            curr_num = nums[idx_i]

            # only pop items from the heap when the window becomes invalid;
            while priority_q and (idx_i - priority_q[0][1]) >= k:
                heapq.heappop(priority_q)
            
            heapq.heappush(priority_q, (-curr_num, idx_i))  
            sliding_window_maxms.append(-priority_q[0][0])

        return sliding_window_maxms


        