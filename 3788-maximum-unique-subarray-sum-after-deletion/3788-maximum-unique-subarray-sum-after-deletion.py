class Solution:
    def maxSum(self, nums: List[int]) -> int:
        '''
        # Solution 1: Using Kadane's Algo
        unique_els = set(nums)

        curr_sub_arr_sum = 0
        max_sub_arr_sum = -101

        for num in unique_els:
            if num < 0:
                max_sub_arr_sum = max(max_sub_arr_sum, num)
                continue
                
            curr_sub_arr_sum = max(curr_sub_arr_sum + num, num)
            max_sub_arr_sum = max(max_sub_arr_sum, curr_sub_arr_sum)
        
        return max_sub_arr_sum
        '''

        '''
        # Solution 2: Most Optimized Hint Solution:
        unique_els = set()
        max_sub_arr_sum = -101

        for num in nums:
            max_sub_arr_sum = max(max_sub_arr_sum, num)
            unique_els.add(num)

        # if the max element in arr is less than or equal than zero
        # then the answer is the max element
        if max_sub_arr_sum <= 0:
            return max_sub_arr_sum

        max_sub_arr_sum = 0
        # Otherwise, the max sum is sum of all unique
        # vals greater than or equal to zero
        for num in unique_els:
            if num > 0:
                max_sub_arr_sum += num
        
        return max_sub_arr_sum
        '''

        '''
        # Solution 3: Most Optimized Hint Solution: & Array Map
        unique_els = [0] * 101
        max_sub_arr_sum = -101

        for num in nums:
            max_sub_arr_sum = max(max_sub_arr_sum, num)
            
            if num >= 0:
                unique_els[num] = num

        # if the max element in arr is less than or equal than zero
        # then the answer is the max element
        if max_sub_arr_sum <= 0:
            return max_sub_arr_sum

        max_sub_arr_sum = 0
        # Otherwise, the max sum is sum of all unique
        # vals greater than or equal to zero
        for num in unique_els:
            if num > 0:
                max_sub_arr_sum += num
        
        return max_sub_arr_sum
        '''
        
        # Hint Comment: 
        # Find the sum of all the unique positive elements first if your
        # maxSum is still like -101 or float('-inf') then
        # find the maxElement in the given nums arr & that is your ans.
        # Solution 4: Most Optimized Hint Solution: & Array Map

        unique_els = [0] * 101
        max_sub_arr_sum = 0

        for num in nums:
            if num > 0 and unique_els[num] == 0:
                max_sub_arr_sum += num
                unique_els[num] = num

        # if maxSum is not -101 or float('-inf') then
        # this is the answ
        if max_sub_arr_sum != 0:
            return max_sub_arr_sum

        max_sub_arr_sum = -101
        # Otherwise, the max sum is the maxElement
        # in the given nums arr 
        for num in nums:
            max_sub_arr_sum = max(max_sub_arr_sum, num)
        
        return max_sub_arr_sum

