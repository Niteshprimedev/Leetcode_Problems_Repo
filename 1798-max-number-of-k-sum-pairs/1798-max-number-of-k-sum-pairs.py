class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Logic: Sort the nums array using built-in or sorting algos
        # and then use two pointers technique to find k-sum pairs;
        
        '''
        # Solution 3: Using Hashmap and No Sorting;
        # Just need to count unique pairs equal k-sum;
        max_pairs_count = 0

        right_side_els_map = defaultdict(int)

        for num in nums:
            right_side_els_map[num] += 1
        
        for first_num in nums:
            right_side_els_map[first_num] -= 1

            second_num = k - first_num

            if right_side_els_map[second_num] > 0 and right_side_els_map[first_num] >= 0:
                max_pairs_count += 1
                right_side_els_map[second_num] -= 1
        
        return max_pairs_count
        '''
        
        # Solution 4: Using Hashmap and No Sorting;
        # Just need to count unique pairs equal k-sum;
        # Only Pass Solution
        max_pairs_count = 0

        nums_els_map = defaultdict(int)

        for first_num in nums:
            second_num = k - first_num

            if nums_els_map[second_num] > 0:
                max_pairs_count += 1
                nums_els_map[second_num] -= 1
            else:
                nums_els_map[first_num] += 1
        
        return max_pairs_count





