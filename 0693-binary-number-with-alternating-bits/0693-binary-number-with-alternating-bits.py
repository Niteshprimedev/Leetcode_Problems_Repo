class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        last_bit = n & 1
        n = n >> 1

        while(n > 0):
            curr_bit = n & 1

            if(curr_bit == last_bit):
                return False
            
            last_bit = curr_bit
            n = n >> 1
        
        return True
        