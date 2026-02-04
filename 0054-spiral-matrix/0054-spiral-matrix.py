class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Solved during DSA Session 9 on May 31
        
        # Observation: It works fine for odd number of rows and odd num of cols
        # when we don't break the loop when the strt_row becomes equal to end_row
        # or when strt_col becomes end_col.
        # But it doesn't work for the even number of cols

        rows = len(matrix)
        cols = len(matrix[0])

        strt_row_idx = 0
        end_row_idx = rows - 1
        strt_col_idx = 0
        end_col_idx = cols - 1

        spiral_matrix_els_list = []

        while((strt_row_idx <= end_row_idx) and (strt_col_idx <= end_col_idx)):

            # Top Boundary:
            # Run a loop from the strt column upto the end column + 1 cause
            # range function will not include the current element 
            for idx_i in range(strt_col_idx, end_col_idx + 1):
                curr_el = matrix[strt_row_idx][idx_i]
                spiral_matrix_els_list.append(curr_el)

            # Right Boundary:
            # Run a loop from the strt row + 1 upto the end row + 1 
            # cause we want to skip the first row cell & include 
            # the last row cell
            for idx_j in range(strt_row_idx + 1, end_row_idx + 1):
                curr_el = matrix[idx_j][end_col_idx]
                spiral_matrix_els_list.append(curr_el)

            if (strt_row_idx == end_row_idx) or (strt_col_idx == end_col_idx):
                break

            # Bottom Boundary:
            # Run a loop from end col - 1 upto the strt col - 1
            # cause we need to skip the last col cell & include the strt col cell
            for idx_i in range(end_col_idx - 1, strt_col_idx - 1, -1):
                curr_el = matrix[end_row_idx][idx_i]
                spiral_matrix_els_list.append(curr_el)

            # Left Boundary:
            # Run a loop from end row - 1 upto the strt row
            # cause we need to skip the last row cell & the strt row cell
            for idx_j in range(end_row_idx - 1, strt_row_idx, -1):
                curr_el = matrix[idx_j][strt_col_idx]
                spiral_matrix_els_list.append(curr_el)

            strt_row_idx += 1
            end_row_idx -= 1
            strt_col_idx += 1
            end_col_idx -= 1
        
        return spiral_matrix_els_list