class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=set()
        column=set()
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(c):
                matrix[i][j]=0
        for j in column:
            for i in range(r):
                matrix[i][j]=0