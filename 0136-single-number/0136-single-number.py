class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        # Solution 1: Using XOR Operator
        # The elements with frequency of 2 or even frequencies
        # will result in 0, and then only element with frequency
        # 1 will generate the answer;
        
        single_num = 0

        for num in nums:
            single_num = single_num ^ num
        
        return single_num
        '''

        # Solution 2: Using The Modulo Operator & Bitwise Pattern 
        # This approach is helpful to solve the Single Number II
        # Idea is to check each of the 32 bits if they are divisible by 2
        # then the bit for the answer will not be set, cause they are repeating
        # and if the bits count are not divisible by 2 then the bit for the answer
        # will be set so we set the bit and return the answer;
        
        # T.C: O(31 * N)
        single_num = 0

        # check each bit position from (0 - 31)
        for bit_idx in range(32):
            set_bits_count = 0

            # count how many 1s or (set bits) are at current position
            left_shift_op_val = (1 << bit_idx)

            for num in nums:
                if (left_shift_op_val & num) != 0:
                    # print('left shift', left_shift_op_val, num, bit_idx)
                    set_bits_count += 1

            # if the last bit is 1 then it's odd else it's even;
            # if the odd count of 1 bits, this bit is set in our answer too
            if (set_bits_count & 1) == 1:
                single_num = single_num | (1 << bit_idx)
        
        # Handle the negative numbers case:
        if single_num & (1 << 31):
            # if the last bit is a sign bit then
            single_num = single_num - (1 << 32)
        
        return single_num