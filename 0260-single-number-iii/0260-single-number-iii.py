class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Use the distinguishing bit (rightmost set bit)
        # to separate them into two groups and XOR within
        # each group to isolate the unique numbers?
        
        two_nums_xor = 0

        for num in nums:
            two_nums_xor = two_nums_xor ^ num
        
        # print(two_nums_xor, two_nums_xor ^ 5)
        bit_pos_diff = ((two_nums_xor & (two_nums_xor - 1)) ^ two_nums_xor)

        # print(bit_pos_diff)

        first_num = 0
        second_num = 0

        for num in nums:
            if (bit_pos_diff & num) == bit_pos_diff:
                first_num = first_num ^ num
            else:
                second_num = second_num ^ num
        
        return [first_num, second_num]
        
