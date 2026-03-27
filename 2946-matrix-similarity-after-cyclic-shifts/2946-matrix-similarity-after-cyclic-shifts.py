class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        copied_mat = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                copied_mat[i][j] = mat[i][j]

        
        def cyclically_shift_left(row_idx, mat):
            first_el = mat[row_idx][0]
            n_cols = len(mat[0])

            for j in range(n_cols - 1):
                mat[row_idx][j] = mat[row_idx][j + 1]
            
            mat[row_idx][n_cols - 1] = first_el

        def cyclically_shift_right(row_idx, mat):
            n_cols = len(mat[0])
            last_el = mat[row_idx][n_cols - 1]

            for j in range(n_cols - 1, 0, -1):
                mat[row_idx][j] = mat[row_idx][j - 1]
            
            mat[row_idx][0] = last_el

        # operations k times;
        while(k > 0):
            
            for i in range(m):
                # shift to left
                if i % 2 == 0:
                    cyclically_shift_left(i, copied_mat)
                # shift to right
                else:
                    cyclically_shift_right(i, copied_mat)

            k -= 1
            
        def check_identical(mat1, mat2):
            m = len(mat1)
            n = len(mat1[0])

            for i in range(m):
                for j in range(n):
                    if mat1[i][j] != mat2[i][j]:
                        return False
            
            return True

        return check_identical(mat, copied_mat)