class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        
        def digits_sum(num):
            sum = 0

            while (num > 0):
                sum += num % 10
                num = num // 10
            
            return sum
        
        largest_groups_count = 0
        largest_group_size = 0

        largest_groups_map = {}

        for num in range(1, n + 1):
            digit = digits_sum(num)
            largest_groups_map[digit] = largest_groups_map.get(digit, 0) + 1

            if largest_groups_map[digit] > largest_group_size:
                largest_group_size = largest_groups_map[digit]
                largest_groups_count = 1
            elif largest_groups_map[digit] == largest_group_size:
                largest_groups_count += 1

        
        # print(largest_groups_map)

        # for key, value in largest_groups_map.items():
        #     largest_group_size = max(largest_group_size, value)

        # for key, value in largest_groups_map.items():
        #     if value == largest_group_size:
        #         largest_groups_count += 1
    
        return largest_groups_count
        

