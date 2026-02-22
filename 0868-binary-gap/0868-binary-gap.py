class Solution:
    def binaryGap(self, n: int) -> int:
        
        max_bin_gap = 0
        prev_bit = -1
        gap_count = 0

        while n > 0:
            curr_bit = n & 1

            if(curr_bit == 0 and prev_bit == 1):
                gap_count += 1
            elif (curr_bit == 1 and prev_bit == 1):
                max_bin_gap = max(max_bin_gap, gap_count)
                gap_count = 1
            elif (curr_bit == 1 and prev_bit == -1):
                prev_bit = 1
                gap_count = 1
            
            n = n >> 1

        return max_bin_gap