import math
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        square_size = 2*k + 1

        # ceil number of squares for the rows;
        min_sensors_count = math.ceil(n/square_size)
        
        # ceil number of squares for the rows;
        min_sensors_count *= math.ceil(m/square_size)

        return min_sensors_count