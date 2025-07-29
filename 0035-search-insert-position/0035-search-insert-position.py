class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Find the lower bound;
        arr_len = len(nums)

        if arr_len == 0:
            return 0
        
        left_idx = 0
        right_idx = arr_len - 1

        first_idx = -1

        while(left_idx <= right_idx):
            middle_idx = left_idx + (right_idx - left_idx) // 2


            if nums[middle_idx] > target:
                right_idx = middle_idx - 1
            elif nums[middle_idx] <= target:
                left_idx = middle_idx + 1
                first_idx = middle_idx
        
        return first_idx if nums[first_idx] == target else first_idx + 1