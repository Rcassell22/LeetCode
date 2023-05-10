class Solution(object):
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned rules.

        Used GPT for this one, will come back and try it again once I solve an easy Sudoku problem
        on my own. As usual, I fed it a few shot exemplar using the first test case in the problem.

        I've noticed a lot of the medium and hard problems build off of knowledge/solutions
        from easy problems covering the same topic.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    box_index = (i // 3) * 3 + (j // 3)
                    if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box_index].add(val)
        return True