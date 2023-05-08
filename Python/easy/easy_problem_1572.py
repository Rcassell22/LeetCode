class Solution(object):
    def diagonal_sum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int

        Somehow this beat 100% of other Python solutions on Leetcode
        """
        height = len(mat)
        height_counter = 0

        width = len(mat[0])
        inverse_width = -abs(width)
        width_counter = 0
        diag_sum = 0

        while width_counter < width and height_counter < height:
            diag_sum += mat[height_counter][width_counter]
            mat[height_counter][width_counter] = 0
            height_counter += 1
            width_counter += 1

        if height != 1:
            width_counter = -1
            height_counter = 0
            while width_counter >= inverse_width and height_counter < height:
                diag_sum += mat[height_counter][width_counter]
                mat[height_counter][width_counter] = 0
                height_counter += 1
                width_counter += -1

        return diag_sum