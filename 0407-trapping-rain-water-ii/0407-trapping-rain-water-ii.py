class Solution:
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col

        def __lt__(self, other):
            return self.height < other.height
    
    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        num_of_rows = len(heightMap)
        num_of_cols = len(heightMap[0])

        visited = [[False] * num_of_cols for _ in range(num_of_rows)]

        boundary = []

        for i in range(num_of_rows):
            heapq.heappush(boundary, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, self.Cell(heightMap[i][num_of_cols - 1], i, num_of_cols - 1))

            visited[i][0] = visited[i][num_of_cols - 1] = True

        for i in range(num_of_cols):
            heapq.heappush(boundary, self.Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary, self.Cell(heightMap[num_of_rows - 1][i], num_of_rows - 1, i))
            visited[0][i] = visited[num_of_rows - 1][i] = True

        total_water_volume = 0

        while boundary:
            # Pop the cell with the smallest height from the boundary
            current_cell = heapq.heappop(boundary)

            current_row = current_cell.row
            current_col = current_cell.col
            min_boundary_height = current_cell.height

            # Explore all 4 neighboring cells
            for direction in range(4):
                # Calculate the row and column of the neighbor
                neighbor_row = current_row + d_row[direction]
                neighbor_col = current_col + d_col[direction]

                # Check if the neighbor is within the grid bounds and not yet visited
                if (
                    self._is_valid_cell(
                        neighbor_row, neighbor_col, num_of_rows, num_of_cols
                    )
                    and not visited[neighbor_row][neighbor_col]
                ):
                    # Get the height of the neighbor cell
                    neighbor_height = heightMap[neighbor_row][neighbor_col]

                    # If the neighbor's height is less than the current boundary height, water can be trapped
                    if neighbor_height < min_boundary_height:
                        # Add the trapped water volume
                        total_water_volume += (
                            min_boundary_height - neighbor_height
                        )

                    # Push the neighbor into the boundary with updated height (to prevent water leakage)
                    heapq.heappush(
                        boundary,
                        self.Cell(
                            max(neighbor_height, min_boundary_height),
                            neighbor_row,
                            neighbor_col,
                        ),
                    )
                    visited[neighbor_row][neighbor_col] = True

        # Return the total amount of trapped water
        return total_water_volume