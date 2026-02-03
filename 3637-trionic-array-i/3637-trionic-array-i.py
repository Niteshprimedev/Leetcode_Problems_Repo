class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        is_inc = False
        is_dec = False
        is_dec_inc = False

        idx_j = 1
        for idx in range(idx_j, len(nums)):
            if nums[idx_j] > nums[idx_j - 1]:
                idx_j += 1
                is_inc = True
            else:
                break

        if idx_j == 1 or idx_j == len(nums):
            return False

        for idx in range(idx_j, len(nums)):
            if nums[idx_j] < nums[idx_j - 1]:
                idx_j += 1
                is_dec = True
            else:
                break

        if idx_j == len(nums):
            return False

        for idx in range(idx_j, len(nums)):
            if nums[idx_j] > nums[idx_j - 1]:
                idx_j += 1
                is_dec_inc = True
            else:
                is_dec_inc = False
                break
                
        if is_inc and is_dec and is_dec_inc:
            return True

        return False