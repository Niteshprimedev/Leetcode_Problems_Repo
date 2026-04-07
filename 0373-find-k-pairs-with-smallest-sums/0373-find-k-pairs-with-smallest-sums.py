class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Logic: Using Python's MaxHeap;
        '''
        # TLE Solution;
        max_heap = []

        idx_i = 0
        idx_j = 0

        sum_count = k
        while idx_i < len(nums1):
            if sum_count == 0:
                break
            
            pair_sum = nums1[idx_i] + nums2[idx_j]
            max_heap.append((-pair_sum, nums1[idx_i], nums2[idx_j]))

            idx_j += 1
            sum_count -= 1
            if idx_j == len(nums2):
                idx_j = 0
                idx_i += 1
        
        heapq.heapify(max_heap)
        for idx2 in range(idx_j, len(nums2)):
            if idx_i < len(nums1):
                pair_sum = nums1[idx_i] + nums2[idx2]

                heapq.heappush(max_heap, (-pair_sum, nums1[idx_i], nums2[idx2]))
                heapq.heappop(max_heap)

        for idx1 in range(idx_i + 1, len(nums1)):
            for idx2 in range(len(nums2)):
                pair_sum = nums1[idx1] + nums2[idx2]

                heapq.heappush(max_heap, (-pair_sum, nums1[idx1], nums2[idx2]))
                heapq.heappop(max_heap)
        
        # print(max_heap)
        # heapq.heapify(max_heap)

        return [[num1, num2] for max_val, num1, num2, in max_heap]
        '''

        '''
        # Solution 2: The Best Way to use PQ;
        # and build smallest pairs;
        from heapq import heappush, heappop

        smallest_pairs = []
        min_heap = []
        m = len(nums1)
        n = len(nums2)

        idx_i = 0
        idx_j = 0

        visited_pairs = set()
        heappush(min_heap, (nums1[idx_i] + nums2[idx_j], (idx_i, idx_j)))
        visited_pairs.add((idx_i, idx_j))

        sum_count = k
        while sum_count > 0 and min_heap:
            pairs_sum, (idx_i, idx_j) = heappop(min_heap)

            pair_sum = nums1[idx_i] + nums2[idx_j]
            smallest_pairs.append([nums1[idx_i], nums2[idx_j]])

            if idx_i + 1 < m and (idx_i + 1, idx_j) not in visited_pairs:
                heappush(min_heap, (nums1[idx_i + 1] + nums2[idx_j], (idx_i + 1, idx_j)))
                visited_pairs.add((idx_i + 1, idx_j))
            
            if idx_j + 1 < n and (idx_i, idx_j + 1) not in visited_pairs:
                heappush(min_heap, (nums1[idx_i] + nums2[idx_j + 1], (idx_i, idx_j + 1)))
                visited_pairs.add((idx_i, idx_j + 1))

            sum_count -= 1

        return smallest_pairs
        '''
        
        # Solution 3: Removed unnecessary variables
        # The best way to use PQ;
        # and build smallest pairs;
        from heapq import heappush, heappop

        smallest_pairs = []
        min_heap = []
        m = len(nums1)
        n = len(nums2)

        idx_i = 0
        idx_j = 0

        visited_pairs = set()
        heappush(min_heap, (nums1[idx_i] + nums2[idx_j], (idx_i, idx_j)))
        visited_pairs.add((idx_i, idx_j))

        sum_count = k
        while sum_count > 0 and min_heap:
            pairs_sum, (idx_i, idx_j) = heappop(min_heap)

            smallest_pairs.append([nums1[idx_i], nums2[idx_j]])

            if idx_i + 1 < m and (idx_i + 1, idx_j) not in visited_pairs:
                heappush(min_heap, (nums1[idx_i + 1] + nums2[idx_j], (idx_i + 1, idx_j)))
                visited_pairs.add((idx_i + 1, idx_j))
            
            if idx_j + 1 < n and (idx_i, idx_j + 1) not in visited_pairs:
                heappush(min_heap, (nums1[idx_i] + nums2[idx_j + 1], (idx_i, idx_j + 1)))
                visited_pairs.add((idx_i, idx_j + 1))

            sum_count -= 1

        return smallest_pairs
            