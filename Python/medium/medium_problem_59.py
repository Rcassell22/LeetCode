class Solution(object):
    def generate_matrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Given a positive integer n, generate an n x n matrix filled
        with elements from 1 to n2 in spiral order.

        Got this one on my own by repurposing the solution from medium_problem_54, which at the time
        I used GPT to create for me. Still a win in my book.

        Basically just create the matrix with all zeros, and then instead of appending to an
        array in spiral order, set the value in the matrix to the number it should be in spiral order.

        Beat 71.14% in runtime and 89.93% in memory usage, not bad.
        """
        if not n:
            return []

        result = []
        result_row = []
        for i in range(0, n):
            result_row.append(0)
        for i in range(0, n):
            result.append(result_row[:])

        element_counter = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result[top][i] = element_counter
                element_counter += 1
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = element_counter
                element_counter += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result[bottom][i] = element_counter
                    element_counter += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result[i][left] = element_counter
                    element_counter += 1
                left += 1

        return result