class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        # So this is how the permutations look like:
        # i = 0 & j = 0, 1, 2 (i will swap with all three js)
        # i = 1 & j = 1, 2 (i will swap with all two js)
        # i = 2 & j = 2 (i will swap with one j)

        # Using Letter Phone Combination Question:

        # for loop will be used:
        permutations_arr = []
        arr_len = len(nums)

        def backtrack_permutations(curr_idx, nums_arr):
            # Base Case:
            if curr_idx == (arr_len - 1):
                permutations_arr.append(nums_arr[:])
                return # back track for other permutations:

            # Recursive Case:
            for swap_idx in range(curr_idx, arr_len):
                [nums_arr[curr_idx], nums_arr[swap_idx]] = [nums_arr[swap_idx], nums_arr[curr_idx]]

                backtrack_permutations(curr_idx + 1, nums_arr)

                # Backtracking step to revert swap changes:
                [nums_arr[curr_idx], nums_arr[swap_idx]] = [nums_arr[swap_idx], nums_arr[curr_idx]]

        backtrack_permutations(0, nums)
    
        return permutations_arr
        '''

        # Solved during DSA Sesison on June 1
        # DK Sir: Solution;
        permutations_arr = []
        curr_output = []
        n = len(nums)

        def backtrack_permutations(nums_arr, n, curr_output, permutations_arr):
            # Base Case:
            if n == 0:
                permutations_arr.append(curr_output)

            for idx_i in range(n):
                new_nums_arr = nums_arr[:idx_i] + nums_arr[idx_i + 1:]
                new_output = curr_output + [nums_arr[idx_i]]

                backtrack_permutations(new_nums_arr, n - 1, new_output, permutations_arr)

        backtrack_permutations(nums, n, curr_output, permutations_arr)

        return permutations_arr
