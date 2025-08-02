class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        # DSA May 4 Question solution by DK Sir!
        # Logic: Reasoning for moving smaller height pointer is
        # if I move my larger height pointer then I might miss on
        # trapping more waters if I might have a larger bar on the left or right;
        # that's why smaller height pointer
        # 6 10 2 8: max amount of water can be trapped is with 10 & 8
        # and not by moving my right pointer i.e bar height 8;
        
        height_len = len(height)
        total_trapped_water_units = 0

        max_right_boundary_suffix = [0] * (height_len)
        
        max_left = height[0]
        max_right = height[height_len - 1]

        for height_idx in range(height_len - 1, -1, -1):
            curr_height = height[height_idx]

            max_right = max(curr_height, max_right)

            max_right_boundary_suffix[height_idx] = max_right
        
        for height_idx in range(height_len):
            curr_height = height[height_idx]

            max_left = max(max_left, curr_height)
            max_right = max_right_boundary_suffix[height_idx]

            curr_boundary = min(max_left, max_right)

            water_trapped_units = max(curr_boundary - curr_height, 0)

            total_trapped_water_units += water_trapped_units

        return total_trapped_water_units
        '''

        # Solution 2: Two pointers Logic;

        height_len = len(height)

        total_trapped_water_units = 0

        leftIdx = 0
        rightIdx = height_len - 1

        max_left = float('-inf')
        max_right = float('-inf')

        while leftIdx < rightIdx:
            max_left = max(max_left, height[leftIdx])
            max_right = max(max_right, height[rightIdx])

            if max_left <= max_right:
                total_trapped_water_units += max_left - height[leftIdx]
                leftIdx += 1
            else:
                total_trapped_water_units += max_right - height[rightIdx]
                rightIdx -= 1

        return total_trapped_water_units
