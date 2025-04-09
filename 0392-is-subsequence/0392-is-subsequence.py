class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str_s_idx = 0
        str_t_idx = 0

        while str_s_idx < len(s) and str_t_idx < len(t):
            if s[str_s_idx] == t[str_t_idx]:
                str_s_idx += 1
            
            str_t_idx += 1
        
        return str_s_idx == len(s)