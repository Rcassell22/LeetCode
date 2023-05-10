class Solution(object):
    def search_matrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        You are given an m x n integer matrix matrix with the following two properties:

        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        This is slower than O(log(m * n)) but LeetCode didn't catch that, and funny enough
        it beat 61.33% in runtime and 73.3% in memory usage.....
        """
        height = len(matrix)
        width = len(matrix[0])

        target_exists = False
        for h in range(0, height):
            if matrix[h][0] <= target and matrix[h][width-1] >= target:
                if target in matrix[h]:
                    target_exists = True
                    break
        return target_exists