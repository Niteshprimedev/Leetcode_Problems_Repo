class Solution:
    def minimumDeletions(self, s: str) -> int:
        # pos_map = defaultdict(list)

        # for idx in range(len(s)):
        #     curr = s[idx]

        #     pos_map[idx] = [pos_map[idx][0], pos_map[idx][1]]
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0

        # First pass: compute count_b which stores the number of
        # 'b' characters to the left of the current position.
        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b":
                b_count += 1

        a_count = 0
        # Second pass: compute count_a which stores the number of
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        # Third pass: iterate through the string to find the minimum deletions
        for i in range(n):
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions


        '''
        # Meta Prep Time Practice
        # Solution using a_count_pos & b_count_pos
        # and the min freq of the chars a or b

        n = len(s)
        b_char_first_pos = -1
        a_char_last_pos = n

        for i in range(n):
            if b_char_first_pos == -1 and s[i] == 'b':
                b_char_first_pos = i
            elif a_char_last_pos == n and s[n - 1 - i] == 'a':
                a_char_last_pos = n - 1 - i
            
            if b_char_first_pos != -1 and a_char_last_pos != n:
                break
        
        # Edge case: if only all a chars or all b chars then 0
        if b_char_first_pos == -1 or a_char_last_pos == n:
            return 0

        a_count = 0
        b_count = 0

        print(b_char_first_pos, a_char_last_pos, len(s))
        strt = b_char_first_pos

        while(strt <= a_char_last_pos):
            if s[strt] == 'b':
                b_count += 1
            
            if s[strt] == 'a':
                a_count += 1
            
            strt += 1

        min_deletions = min(a_count, b_count)
        return min_deletions
        '''