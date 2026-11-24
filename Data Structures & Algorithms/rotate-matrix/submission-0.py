# Attempt again

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) # all  rows of the matrix

        # move 1: transpose (swap (r, c) with (c, r), each pair once)
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # move 2: ____
        for row in matrix:
            row.reverse()