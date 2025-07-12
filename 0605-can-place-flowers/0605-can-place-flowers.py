class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        '''
        # Solution1:
        can_plant_flowers = False

        for plot_idx in range(len(flowerbed)):
            if n == 0:
                break
                
            curr_plot = flowerbed[plot_idx]

            prev_plot = 0
            if plot_idx > 0:
                prev_plot = flowerbed[plot_idx - 1]
            
            next_plot = 0
            if plot_idx < len(flowerbed) - 1:
                next_plot = flowerbed[plot_idx + 1]
            
            # Greedily plant the flowers whenever a plot exists;
            if curr_plot == 0 and prev_plot == 0 and next_plot == 0:
                flowerbed[plot_idx] = 1
                n -= 1
        
        return n == 0
        '''

        # Solution2: Just count the possible flowers planting;
        total_empty_plots = 0

        can_plant_flowers = False
        
        for plot_idx in range(len(flowerbed)):
            curr_plot = flowerbed[plot_idx]

            prev_plot = 0
            if plot_idx > 0:
                prev_plot = flowerbed[plot_idx - 1]
            
            next_plot = 0
            if plot_idx < len(flowerbed) - 1:
                next_plot = flowerbed[plot_idx + 1]
            
            if prev_plot == 0 and curr_plot == 0 and next_plot == 0:
                total_empty_plots += 1
                flowerbed[plot_idx] = 1
            
            if total_empty_plots == n:
                break

        if total_empty_plots >= n:
            can_plant_flowers = True

        return can_plant_flowers