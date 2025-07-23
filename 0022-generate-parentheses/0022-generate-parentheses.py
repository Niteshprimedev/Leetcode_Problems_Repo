class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        # Logic: Similar to Generate IP Address with four blocks of 
        # array elements and then you try the first 3 blocks as full
        # and the last block as empty or as many nums as possible;

        # Pre-Req: https://leetcode.com/problems/restore-ip-addresses/description/

        total_size = n * 2
        all_parenthe_combs = []
        curr_comb = [''] * total_size
        curr_comb[0] = '('
        curr_comb[total_size - 1] = ')'

        # print(curr_comb)

        def is_valid_parenthe(parenthe_list):
            parenthe_stack = []

            for parenthe in parenthe_list:
                if not parenthe_stack or parenthe == '(':
                    parenthe_stack.append(parenthe)
                elif parenthe_stack and parenthe_stack[-1] == '(':
                    parenthe_stack.pop()
                else:
                    return False
            
            if len(parenthe_stack) > 0:
                return False

            # print(parenthe_stack, parenthe_list)
            return True

        def generate_parenthe_combs(curr_idx, curr_comb):
            # Base Case:
            if curr_idx == (total_size - 1):
                # print(curr_comb)
                if is_valid_parenthe(curr_comb):
                    all_parenthe_combs.append(''.join(curr_comb))
                return
            
            # Recursive Case:
            for curr_parenthe in '()':
                # print(curr_comb, curr_idx, curr_parenthe)
                curr_comb[curr_idx] = curr_parenthe
                generate_parenthe_combs(curr_idx + 1, curr_comb)

                # backtrack and revert changes for next parenthesis generation
                curr_comb[curr_idx] = ''                

        generate_parenthe_combs(1, curr_comb)

        return all_parenthe_combs
        '''

        # Solution 2: Solution Ref:
        # https://leetcode.com/problems/generate-parentheses/solutions/6048157/video-increase-number-of-open-parentheses-until-we-reach-n-at-first
        all_parenthe_combs = []

        def dfs(open_pare, close_pare, s):
            if open_pare == close_pare and open_pare + close_pare == n * 2:
                all_parenthe_combs.append(s)
                return
            
            if open_pare < n:
                dfs(open_pare + 1, close_pare, s + "(")
            
            if close_pare < open_pare:
                dfs(open_pare, close_pare + 1, s + ")")

        dfs(0, 0, "")

        return all_parenthe_combs

