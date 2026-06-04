class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        sol = []
        col = set()
        pos = set()
        neg = set()
        def bt(r):
            if r == n:
                sol.append([''.join(row) for row in board])
            for c in range(n):
                if c in col or r+c in pos or r-c in neg:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)

                bt(r+1)

                board[r][c] = '.'
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        bt(0)
        return sol