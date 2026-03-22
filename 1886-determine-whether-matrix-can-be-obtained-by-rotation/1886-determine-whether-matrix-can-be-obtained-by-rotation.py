class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Using Rotate Image Technique

        def rotate_mat(mat):
            # transpose of a matrix first;
            for row_idx in range(len(mat)):
                for col_idx in range(row_idx + 1, len(mat)):
                    temp_val = mat[row_idx][col_idx]
                    mat[row_idx][col_idx] = mat[col_idx][row_idx]
                    mat[col_idx][row_idx] = temp_val
                
            # now reverse the col of the mat for clockwise
            for row_idx in range(len(mat)):
                strt_col = 0

                for end_col in range(len(mat) - 1, -1, -1):
                    if(strt_col >= end_col): break

                    first_val = mat[row_idx][strt_col]
                    last_val = mat[row_idx][end_col]

                    mat[row_idx][strt_col] = last_val
                    mat[row_idx][end_col] = first_val
                    strt_col += 1
                
            # for row_idx in range(len(mat)):
            #     for col_idx in range(len(mat)):
                    # print(mat[row_idx][col_idx])

        def check_target(mat, target):
            n = len(mat)
            
            for row_idx in range(n):
                for col_idx in range(n):
                    if mat[row_idx][col_idx] != target[row_idx][col_idx]:
                        return False
            
            return True
        
        if(check_target(mat, target)):
            return True
        # print("Hello")
        
        for i in range(3):
            rotate_mat(mat)

            if(check_target(mat, target)):
                return True
        
        return False