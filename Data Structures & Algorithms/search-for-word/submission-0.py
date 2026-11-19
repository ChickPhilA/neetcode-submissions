class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(r, c, matched):
            if matched == len(word):
                return True

            # out of bounds case
            if r < 0 or c < 0 or r > rows-1 or c > cols-1:
                return False

            # visited tile case
            if visited[r][c]:
                return False

            # wrong-letter case
            if board[r][c] != word[matched]:
                return False

            visited[r][c] = True # marking it as visited

            if (backtrack(r-1, c, matched + 1) or
                backtrack(r, c+1, matched + 1) or
                backtrack(r, c-1, matched + 1) or
                backtrack(r+1, c, matched + 1)):
                return True

            visited[r][c] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False