class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        # Solution using Backtracking and Combinations Logic
        all_combs_list = []

        def generate_combs(curr_idx, curr_comb):
            # Base Case:
            if len(curr_comb) == k:
                all_combs_list.append(curr_comb[:])
                return
            if len(curr_comb) > k or curr_idx > n:
                return

            for idx_i in range(curr_idx, n + 1):
                curr_comb.append(idx_i)
                generate_combs(idx_i + 1, curr_comb)
                curr_comb.pop(len(curr_comb) - 1)
            
        generate_combs(1, [])

        return all_combs_list
        '''
        
        # Solution using Backtracking and Combinations Logic
        # Pick and Not Pick Technique
        all_combs_list = []

        def generate_combs(curr_idx, curr_comb):
            # Base Case:
            if len(curr_comb) == k:
                all_combs_list.append(curr_comb[:])
                return
            if len(curr_comb) > k or curr_idx > n:
                return

            # Pick case:
            curr_comb.append(curr_idx)
            generate_combs(curr_idx + 1, curr_comb)
            curr_comb.pop(len(curr_comb) - 1)

            # Not Pick Case:
            generate_combs(curr_idx + 1, curr_comb)

        generate_combs(1, [])

        return all_combs_list