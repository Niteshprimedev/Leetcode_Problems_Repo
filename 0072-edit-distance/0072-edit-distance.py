class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        # Top Down Approach Solution:
        # with -1 and n - 1 iterations;

        str1_len = len(word1)
        str2_len = len(word2)

        memo_dp = [[-1 for _ in range(str2_len)] for _ in range(str1_len)]

        def all_str_ops(str1_idx, str2_idx):
            # Base Case:
            if str1_idx < 0:
                return str2_idx + 1
            if str2_idx < 0:
                return str1_idx + 1

            if memo_dp[str1_idx][str2_idx] != -1:
                return memo_dp[str1_idx][str2_idx]
            
            # Match Case:
            if word1[str1_idx] == word2[str2_idx]:
                match_case_ops = 0 + all_str_ops(str1_idx - 1, str2_idx - 1)
                memo_dp[str1_idx][str2_idx] = match_case_ops

                return memo_dp[str1_idx][str2_idx]
            
            # Not Match Case:
            else:
                # Insert a Char Case:
                insert_case_ops = 1 + all_str_ops(str1_idx, str2_idx - 1)

                # Delete a Char Case:
                delete_case_ops = 1 + all_str_ops(str1_idx - 1, str2_idx)

                # Replace a Char Case:
                replace_case_ops = 1 + all_str_ops(str1_idx - 1, str2_idx - 1)

                memo_dp[str1_idx][str2_idx] = min(insert_case_ops, delete_case_ops, replace_case_ops)
                return memo_dp[str1_idx][str2_idx]

        return all_str_ops(str1_len - 1, str2_len - 1)
        '''
        # Top Down Approach Solution:
        # With the right shift of indices by 1;

        str1_len = len(word1)
        str2_len = len(word2)

        memo_dp = [[-1 for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]

        def all_str_ops(str1_idx, str2_idx):
            # Base Case:
            if str1_idx == 0:
                return str2_idx # idx are now 1 based;

            if str2_idx == 0:
                return str1_idx # idx are now 1 based;

            if memo_dp[str1_idx][str2_idx] != -1:
                return memo_dp[str1_idx][str2_idx]
            
            # Match Case:
            if word1[str1_idx - 1] == word2[str2_idx - 1]:
                match_case_ops = 0 + all_str_ops(str1_idx - 1, str2_idx - 1)
                memo_dp[str1_idx][str2_idx] = match_case_ops

                return memo_dp[str1_idx][str2_idx]
            
            # Not Match Case:
            else:
                # Insert a Char Case:
                insert_case_ops = 1 + all_str_ops(str1_idx, str2_idx - 1)

                # Delete a Char Case:
                delete_case_ops = 1 + all_str_ops(str1_idx - 1, str2_idx)

                # Replace a Char Case:
                replace_case_ops = 1 + all_str_ops(str1_idx - 1, str2_idx - 1)

                memo_dp[str1_idx][str2_idx] = min(insert_case_ops, delete_case_ops, replace_case_ops)
                return memo_dp[str1_idx][str2_idx]

        return all_str_ops(str1_len, str2_len)