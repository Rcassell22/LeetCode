class Solution(object):
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascals_matrix = []

        for i in range(0, num_rows):
            row = [1]

            j = 1
            while(j < i):
                row.append(pascals_matrix[i-1][j-1] + pascals_matrix[i-1][j])
                j += 1

            if i > 0:
                row.append(1)

            pascals_matrix.append(row)

        return pascals_matrix