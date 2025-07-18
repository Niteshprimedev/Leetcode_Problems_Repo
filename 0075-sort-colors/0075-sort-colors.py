class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        # SDE Sheet Top 50 Interview Questions:

        # sort the red color first:
        color_idx = 0

        for idx_i in range(len(nums)):
            curr_color = nums[idx_i]

            if curr_color <= nums[color_idx] and curr_color == 0:
                nums[idx_i] = nums[color_idx]
                nums[color_idx] = curr_color
                color_idx += 1
        
        # sorting the white color next;
        # print(nums, color_idx)

        if color_idx == len(nums):
            return nums

        for idx_i in range(len(nums)):
            curr_color = nums[idx_i]

            if curr_color <= nums[color_idx] and curr_color == 1:
                nums[idx_i] = nums[color_idx]
                nums[color_idx] = curr_color
                color_idx += 1
            
        return nums
        '''

        '''
        # Counting Sort Algorithm: Good but the solution requires in-place changes
        # so didn't work;
        total_red_colors_count = 0
        total_white_colors_count = 0
        total_blue_colors_count = 0

        for color in nums:
            if color == 0:
                total_red_colors_count += 1
            elif color == 1:
                total_white_colors_count += 1
            else:
                total_blue_colors_count += 1
        
        print(total_red_colors_count, total_white_colors_count, total_blue_colors_count)
        
        for idx_i in range(len(nums)):
            if total_red_colors_count > 0:
                nums[idx_i] = total_red_colors_count
                total_red_colors_count -= 1
                print(0)
            elif total_white_colors_count > 0:
                nums[idx_i] = total_white_colors_count
                total_white_colors_count -= 1
                print(1)
            else:
                nums[idx_i] = total_blue_colors_count
                total_blue_colors_count -= 1
                print(2)
            
            print(nums)
        
        return nums
        '''

        '''
        # Dutch National Flag Algorithm:
        # Logic: Increase both i and j when the j is 0,
        # Increase only j when the j is 1, and decrease only the
        # k when j is 2.

        red_color_idx = 0
        blue_color_idx = len(nums) - 1
        color_idx = 0

        while color_idx <= blue_color_idx:
            # if the color is red color then swap with red
            # and increment red color idx by 1
            if nums[color_idx] == 0:
                nums[red_color_idx], nums[color_idx] = nums[color_idx], nums[red_color_idx]
                red_color_idx += 1
                color_idx += 1
            # if the color is white color then just increment the idx by 1
            elif nums[color_idx] == 1:
                color_idx += 1
            # if the color is blue color then swap it with blue
            # and decrement blue color idx by 1
            elif nums[color_idx] == 2:
                nums[blue_color_idx], nums[color_idx] = nums[color_idx], nums[blue_color_idx]
                blue_color_idx -= 1
        
        # Note: if we place the red and blue colors in their sorted places
        # then the white color is already placed in their sorted places
        return nums
        '''

        # Solution using Quick Sort & Pivot as end;
        def partition(nums, low, high):
            pivot_el = nums[high]

            # start sorting from the unsorted part in array;
            idx_i = low - 1

            for idx_j in range(low, high):
                if nums[idx_j] <= pivot_el:
                    idx_i += 1
                    nums[idx_i], nums[idx_j] = nums[idx_j], nums[idx_i]
                
            idx_i += 1
            nums[idx_i], nums[high] = nums[high], nums[idx_i]

            return idx_i

        def quick_sort(nums, low, high):
            # if there are 2 or more elements to swap then swap it;
            if low < high:
                pivot_idx = partition(nums, low, high)

                quick_sort(nums, low, pivot_idx - 1)
                quick_sort(nums, pivot_idx + 1, high)

                return nums
        
        
        return quick_sort(nums, 0, len(nums) - 1)



