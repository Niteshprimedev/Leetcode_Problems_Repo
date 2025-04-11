class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_nums_count = 0

        for num_val in range(low, high + 1):
            if num_val < 100 and num_val % 11 == 0:
                symmetric_nums_count += 1
            
            if 1000<= num_val < 10000:
                temp_num_val = num_val
                
                right = num_val % 10
                num_val = num_val // 10
                right += num_val % 10
                num_val = num_val // 10
                left = num_val % 10
                num_val = num_val // 10
                left += num_val % 10

                num_val = temp_num_val

                '''
                left = num_val // 1000 + num_val % 1000 // 100 # 1203 // 1000 => 1 and 1203 % 1000 or (203) // 100 => 2
                right = num_val % 100 // 10 + num_val % 10 # 1203 % 100 or ()
                # print(num_val % 100, num_val % 100 // 10, num_val % 10, num_val // 1000);
                '''
                
                if left == right:
                    symmetric_nums_count += 1
    
        return symmetric_nums_count
        '''
        symmetric_nums_count = 0
        def digits_sum(digits):
            sum = 0

            for digit in digits:
                sum += int(digit)
            
            return sum

        def check_symmetric_num_val(num):
            num_str = str(num)
            num_str_len = len(num_str)

            if num_str_len % 2 != 0:
                return False
            
            first_digit_idx = num_str_len // 2
            second_digit_idx = num_str_len // 2

            first_digit_str = num_str[:first_digit_idx]
            second_digit_str = num_str[first_digit_idx:]

            first_digit = digits_sum(first_digit_str)
            second_digit = digits_sum(second_digit_str)

            if first_digit == second_digit:
                return True
            return False

        for idx_i in range(low, high + 1):
            num_val = idx_i

            if num_val <= 11 and high >= 11:
                num_val = 11
                while (num_val % 11 == 0) and (num_val <= high):
                    num_val += num_val
                    symmetric_nums_count += 1
            elif (num_val > 99) and (num_val < 1001) and (high >= 1001):
                num_val = 1001

            is_symmetric = check_symmetric_num_val(num_val)
            if(is_symmetric):
                symmetric_nums_count += 1
            idx_i = num_val
        
        

        return symmetric_nums_count
        '''

