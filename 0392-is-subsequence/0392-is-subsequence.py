class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
            
        is_sub_seq = False

        str_len = 1

        loop_idx = 0
        while loop_idx < str_len:
            str_s_idx = 0
            
            for idx_i in range(len(t)):
                char_s = s[str_s_idx]
                char_t = t[idx_i]

                if char_s == char_t:
                    str_s_idx += 1
                
                if str_s_idx == len(s):
                    is_sub_seq = True
                    break
            
            loop_idx += 1
        
        return is_sub_seq