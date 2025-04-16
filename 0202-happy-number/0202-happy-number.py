class Solution:
    def isHappy(self, n: int) -> bool:
        visited_nums_map = dict()

        def get_next_number(n):
            digits_sum = 0

            while n > 0:
                digit = n % 10
                digits_sum += digit ** 2
                n = n // 10
            
            return digits_sum

        while True:
            slow = get_next_number(n)
            fast = get_next_number(get_next_number(n))

            while slow != fast:
                if fast == 1:
                    return True
                
                slow = get_next_number(slow)
                fast = get_next_number(get_next_number(fast))
            
            if slow == fast or fast == 1:
                break

        # print(n)
        return True if slow == 1 else False