class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Logic: Using Monotonic Stack && Suffix Max;

        nums_len = len(nums)

        if nums_len < 3:
            return False

        prev_smaller_els = []
        suffix_max = [0] * nums_len
        suffix_max[nums_len - 1] = nums[nums_len - 1]

        for idx_i in range(nums_len - 2, 0, -1):
            suffix_max[idx_i] = max(nums[idx_i], suffix_max[idx_i + 1])
        
        print(suffix_max)

        for idx_i in range(nums_len):
            num = nums[idx_i]

            while prev_smaller_els and prev_smaller_els[-1] >= num:
                prev_smaller_els.pop()
            
            prev_smaller_els.append(num)

            if len(prev_smaller_els) >= 2 and prev_smaller_els[-1] < suffix_max[idx_i]:
                return True

        return False

        '''
        # This algorithm to find the first smallest and second smallest
        # is valid to ensure that there exists an increasing triplet but
        # it does not guarantee that the correct indices of i, j, and k;

        first_num = float('inf')
        second_num = float('inf')

        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True
        
        return False
        '''
        