class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascal_triangle = []
        prev_level = [1]

        for row_idx in range(numRows):
            curr_level = [0] * (row_idx + 1)

            for idx in range(row_idx + 1):
                prev_val = prev_level[idx - 1] if idx > 0 else 0
                curr_val = prev_level[idx] if idx < len(prev_level) else 0

                curr_level[idx] = prev_val + curr_val
            
            prev_level = curr_level
            pascal_triangle.append(curr_level)
        
        return pascal_triangle
        