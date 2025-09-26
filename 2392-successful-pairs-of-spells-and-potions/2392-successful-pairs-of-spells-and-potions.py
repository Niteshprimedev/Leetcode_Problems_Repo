class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        # The TLE Recipe
        # Brute Force Solution:

        pairs = [0 for _ in range(len(spells))]
        for idx_i in range(len(spells)):
            spell = spells[idx_i]
            total_pairs = 0

            for potion in potions:
                strength = spell * potion

                if strength >= success:
                    total_pairs += 1
            
            pairs[idx_i] = total_pairs
        
        return pairs
        '''

        # Better Approach: Less than N^2 T.C:
        # Solution using Binary Search and Finding the Lower Bound;

        # Thus, for each spell, we need to find the potion with 
        # the least strength that will form a successful pair.
        # After sorting the potions the answer is easy to figure out using binary search
        # cause all you need to figure out is your target value that when 
        # multiplied with your current spell gives the value at least equal to success
        # or even higher;
        n = len(spells)
        pairs = [0 for _ in range(n)]

        potions = sorted(potions)
        m = len(potions)

        for idx_i in range(n):
            curr_spell = spells[idx_i]

            # Binary Search a target that will give value when 
            # multiplied with current spell greater than or equal
            # to success; and I count the number of elements to the right of it;

            left_idx = 0
            right_idx = m - 1
            strt_pair_idx = -1

            while (left_idx <= right_idx):
                middle_idx = left_idx + (right_idx - left_idx) // 2

                strength = curr_spell * potions[middle_idx]

                if strength >= success:
                    # this is potential pair index;
                    # and find the smaller pair index if possible
                    strt_pair_idx = middle_idx
                    right_idx = middle_idx - 1
                else:
                    # the potential pair index lies in the higher side
                    # find the bigger pair index if possible
                    left_idx = middle_idx + 1
            
            # successful pairs that have at least success
            if strt_pair_idx == -1:
                pairs[idx_i] = 0
            else:
                pairs[idx_i] = m - strt_pair_idx
            
        return pairs
