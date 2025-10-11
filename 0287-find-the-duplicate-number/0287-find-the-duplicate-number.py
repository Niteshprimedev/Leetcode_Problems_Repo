class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        # Counting Sort Solution
        n = len(nums)
        idx_i = 0

        while idx_i < n:
            curr_num = nums[idx_i]

            if (curr_num - 1) != idx_i:
                if curr_num == nums[curr_num - 1]:
                    return curr_num
                else:
                    nums[idx_i], nums[curr_num - 1] = nums[curr_num - 1], nums[idx_i]
            else:
                idx_i += 1
        
        '''

        '''
        # Bit Manipulation

        duplicate_num = 0
        n = len(nums)

        for val in range(1, n):
            duplicate_num = duplicate_num ^ val
        
        for num in nums:
            duplicate_num = duplicate_num ^ num

        return duplicate_num
        # 3, 3, 3, 3, 3 => tricky case; 
        '''

        # slow = 0
        # fast = 0
        # slow += 1
        # fast += 2

        # 1, 3, 4, 2, 2
        # slow = 1, 3, 2
        # fast = 1, 2, 2

        n = len(nums)
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        # slow2 = 1, 3, 2
        # slow = 2, 4, 2

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow      