import math
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        # Intuition: To cover the max number of cells using a censor
        # is to place it in the middle and it can cover k distance
        # to cover all the side cells
        # and if you try to place a censor in the middle and go 
        # and count all the cells around it at k distance then 
        # it will form a square of size (2*k + 1) hence you
        # need the (2*k + 1) size of squares to cover the 
        # entire grid with the censors and to cover the rows
        # you need ceil number of squares for the rows and same for cols;
        # And just multiply the rows * cols to get the ans;
        square_size = 2*k + 1

        # ceil number of squares for the rows;
        min_sensors_count = math.ceil(n/square_size)
        
        # ceil number of squares for the rows;
        min_sensors_count *= math.ceil(m/square_size)

        return min_sensors_count