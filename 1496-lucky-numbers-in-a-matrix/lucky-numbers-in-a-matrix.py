import numpy as np
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row=set()
        col=set()
        matrix=np.array(matrix)
        for rows in matrix:
            row.add(min(rows))
        transpose_matrix=np.transpose(matrix)
        for cols in transpose_matrix:
            col.add(max(cols))
        return row.intersection(col)
        