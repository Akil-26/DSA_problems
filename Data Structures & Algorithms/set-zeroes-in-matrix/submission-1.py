class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,cols = len(matrix),len(matrix[0])
        zero_r,zero_c = set(),set()
        for r in range(row):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_r.add(r)
                    zero_c.add(c)
        for r in range(row):
            for c in range(cols):
                if r in zero_r or c in zero_c:
                    matrix[r][c] = 0