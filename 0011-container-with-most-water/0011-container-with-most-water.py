class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Notes: Greedy Alogrithm - Being greedy
        # about maximizing the height of the container when
        # the width is maximized;
        container_with_most_water = 0

        left_idx = 0
        right_idx = len(height) - 1

        max_left_boundary = height[left_idx]
        max_right_boundary = height[right_idx]

        while left_idx < right_idx:
            max_left_boundary = max(max_left_boundary, height[left_idx])
            max_right_boundary = max(max_right_boundary, height[right_idx])

            new_container_with_most_water = 0
            container_width = right_idx - left_idx

            if max_left_boundary <= max_right_boundary:
                new_container_with_most_water = max_left_boundary * container_width
                left_idx += 1
            else:
                new_container_with_most_water = max_right_boundary * container_width
                right_idx -= 1
            
            container_with_most_water = max(container_with_most_water, new_container_with_most_water)
        
        return container_with_most_water
