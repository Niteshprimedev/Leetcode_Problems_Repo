class Solution:
    def isHappy(self, n: int) -> bool:
        num_els_map = {}

        while(n not in num_els_map):
            num_els_map[n] = True
            digits_sum = 0
            while(n > 0):
                digit = n % 10
                digits_sum += digit ** 2
                n = n // 10
            n = digits_sum
        
        # print(n)
        return True if n == 1 else False