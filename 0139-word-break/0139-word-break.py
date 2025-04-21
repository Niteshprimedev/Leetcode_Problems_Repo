class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a memoization table to store the dynamic programming results
        # The table has a size of len(s) + 1, where memo_dp[i] represents whether
        # the substring s[0:i] can be segmented into words from the word dictionary
        memo_dp = [False] * (len(s) + 1)

        # The empty string can always be segmented, so set memo_dp[0] to True
        memo_dp[0] = True

        # Iterate over the string from left to right
        for curr_idx in range(1, len(s) + 1):

            # For each position, try to find a word in the dictionary that matches
            # the substring ending at the current position
            for word in wordDict:
                # Calculate the start position of the substring
                start_pos = curr_idx - len(word)

                # Extract the substring
                curr_substr = s[start_pos:curr_idx]

                # Check if the start position is valid, the substring can be segmented
                # from the previous position, and the substring matches the current word
                if start_pos >= 0 and memo_dp[start_pos] and curr_substr == word:

                    # If a match is found, set memo_dp[curr_idx] to True and break
                    # the inner loop, as we don't need to check other words
                    memo_dp[curr_idx] = True
                    break
        
        # The result is stored in the last position of the memoization table
        return memo_dp[-1]