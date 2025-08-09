class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        return (n & (n - 1)) == 0 and n > 0
        '''

        num_val = (n & (n - 1))
        
        if num_val == 0 and n > 0:
            return True
        else:
            return False