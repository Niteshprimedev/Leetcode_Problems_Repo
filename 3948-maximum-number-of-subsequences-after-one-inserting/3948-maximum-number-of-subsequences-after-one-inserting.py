class Solution:
    def numOfSubsequences(self, s: str) -> int:

        '''
        # Peers Solution:
        n = len(s)

        prefix_L = [0] * n
        suffix_T = [0] * n
        
        insert_L = 0
        insert_C = 0
        insert_T = 0
        option_C = 0

        for idx in range(n):
            char = s[idx]
            end_idx = n - 1 - idx

            if s[idx] == "L":
                prefix_L[idx] = 1 + prefix_L[idx - 1] if idx > 0 else 1
            else:
                prefix_L[idx] = prefix_L[idx - 1] if idx > 0 else prefix_L[idx]
            if s[end_idx] == "T":
                suffix_T[end_idx] = 1 + suffix_T[end_idx + 1] if (end_idx + 1) < n else 1
            else:
                suffix_T[end_idx] = suffix_T[end_idx + 1] if (end_idx + 1) < n else suffix_T[end_idx]
        
        # print(prefix_L, suffix_T)
        
        for idx in range(n):
            char = s[idx]
            if char == "C":
                insert_L += (prefix_L[idx] + 1) * (suffix_T[idx])
                insert_C += prefix_L[idx] * suffix_T[idx]
                insert_T += (prefix_L[idx]) * (suffix_T[idx] + 1)
            else:
                option_C = max(option_C, prefix_L[idx] * suffix_T[idx])
        
        return max(insert_L, insert_T, insert_C + option_C)
        '''

        # Constant Space Solution: Peers Solution:
        n = len(s)

        prefix_L = 0
        suffix_T = s.count('T')
        
        insert_L = 0
        insert_C = 0
        insert_T = 0
        option_C = 0
        
        for idx in range(n):
            char = s[idx]
            end_idx = n - 1 - idx

            if s[idx] == "L":
                prefix_L += 1 
            elif s[idx] == "T":
                suffix_T -= 1 

            # when char is C then you insert either L, C, T
            # cause we are calculating the LCT subsequences at each C;
            if char == "C":
                insert_L += (prefix_L + 1) * (suffix_T)
                insert_C += prefix_L * suffix_T
                insert_T += (prefix_L) * (suffix_T + 1)
            # when char is not C then you can only insert C
            # cause the char is either LT or any other char
            else:
                option_C = max(option_C, prefix_L * suffix_T)
        
        return max(insert_L, insert_T, insert_C + option_C)

        # Wrong Solution:
        '''
        is_inserted = False
        if "L" not in s:
            is_inserted = True
            s = "L" + s
        elif "C" not in s:
            total_L = s.count('L')
            total_T = 0

            insert_idx = -1
            max_LT = float('-inf')

            for idx in range(len(s) - 1, 0, -1):
                char = s[idx]

                if char == "L":
                    total_L -= 1
                elif char == "T":
                    total_T += 1
                
                curr_LT = total_L * total_T

                if curr_LT > max_LT and total_T > 0 and total_L > 0:
                    max_LT = curr_LT
                    insert_idx = idx
            
            if insert_idx != -1:
                is_inserted = True
                s = s[:insert_idx] + "C" + s[insert_idx:]

        elif "T" not in s:
            is_inserted = True
            s = s + "T"
        
        count_L = 0
        count_LC = 0
        count_LCT = 0
        count_T = 0

        for char in s:
            if char == "L":
                count_L += 1
            elif char == "C":
                count_LC += count_L
            elif char == "T":
                count_T += 1
                count_LCT += count_LC
            
        insert_L = 0

        insert_C = 0

        insert_T = 0

        # print(s, is_inserted)

        if not is_inserted:
            insert_L = count_LC

            insert_C = count_L * s.count('T')

            insert_T = count_LC

        max_subseq = max(count_LCT + insert_L, insert_C + count_LCT, insert_T + count_LCT)

        return max_subseq
        '''