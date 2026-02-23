class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes_map = defaultdict(int)

        strt_idx = 0
        end_idx = 0

        while end_idx < len(s):
            end_idx += 1
            if(end_idx - strt_idx) == k:
                codes_map[s[strt_idx:end_idx]] = 1
                # print(s[strt_idx:end_idx])
                strt_idx += 1

        total_codes = pow(2, k)

        # print(len(codes_map))
        if len(codes_map) == total_codes:
            return True
        
        return False
        
        # 000 -> 001 -> 010 -> 100 -> 111 -> 011 -> 101 -> 110 -> 