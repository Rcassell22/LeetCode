class Solution(object):
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Given an m by n matrix, return all elements of the matrix in spiral order.

        I had GPT 3.5 Turbo generate this one. Yes, I am ashamed.
        I prompted it with the problem, asked it to write it as a Senior Computer Scientist, and used CoT to give it
        a few-shot exemplar of what as correct answer looked like from test_case_1.

        Need to come back to this problem at some point and see if I can figure it out myself.

        GPT's Explanation:

        The function starts by initializing an empty list res to store all the elements of
        the matrix in spiral order. It then gets the number of rows and columns of the matrix,
        and initializes four variables top, bottom, left, and right to represent the boundaries
        of the matrix.

        The function then enters a loop that continues until all the elements of the matrix have
        been added to the result list res. The first step in each iteration is to add the elements
        in the top row of the matrix from left to right. The top boundary is then moved down one row.

        The next step is to add the elements in the right column from top to bottom. The right boundary
        is then moved left by one column.

        If there is still at least one row left in the matrix after moving the top boundary down, the
        function adds the elements in the bottom row from right to left. The bottom boundary is then
        moved up one row.

        If there is still at least one column left in the matrix after moving the right boundary left,
        the function adds the elements in the left column from bottom to top. The left boundary is
        then moved right by one column.

        Once all the elements of the matrix have been added to the result list res, the function
        returns the list.

        Constraints:
            m == matrix.length
            n == matrix[i].length
            1 <= m, n <= 10
            -100 <= matrix[i][j] <= 100
        """
        if not matrix:
            return []

        result = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

