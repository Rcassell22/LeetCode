class Solution(object):
    def matrix_reshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]

        In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into
        a new one with a different size r x c keeping its original data.

        You are given an m x n matrix mat and two integers r and c representing the number of rows
        and the number of columns of the wanted reshaped matrix.

        The reshaped matrix should be filled with all the elements of the original matrix in the same
        row-traversing order as they were.

        If the reshape operation with given parameters is possible and legal, output the new reshaped
        matrix; Otherwise, output the original matrix.


        Somehow this solution beat 99.13% of submissions
        """
        height = len(mat)
        width = len(mat[0])

        reshaped_mat = []
        if r * c != height * width or (r == height and c == width):
            reshaped_mat = mat
        else:
            mat_elements = []
            for i in range(0, height):
                for j in range(0, width):
                    mat_elements.append(mat[i][j])
            for k in range(0, r):
                row = []
                reshaped_mat.append(row)
                for l in range(0, c):
                    reshaped_mat[k].append(mat_elements.pop(0))
        return reshaped_mat