class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills_valleys_count = 0
        n = len(nums)

        # Edge Case;
        if n <= 2:
            return 0

        for idx in range(1, n - 1):
            curr_num = nums[idx]

            prev_idx = idx - 1
            # skip the same valley or hill;
            if curr_num == nums[prev_idx]:
                continue

            while prev_idx >= 0 and nums[prev_idx] == curr_num:
                prev_idx -= 1
            
            next_idx = idx + 1
            while next_idx < n and nums[next_idx] == curr_num:
                next_idx += 1
            
            if prev_idx < 0 or next_idx == n:
                continue

            # print(curr_num)
            # else did we find a hill or valley;
            if nums[prev_idx] < curr_num > nums[next_idx]:
                # case for hill
                hills_valleys_count += 1
            elif nums[prev_idx] > curr_num < nums[next_idx]:
                # case for hill
                hills_valleys_count += 1
        
        return hills_valleys_count
                


        