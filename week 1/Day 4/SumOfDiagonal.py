class Solution(object):
    def diagonalSum(self, mat):
        row = len(mat)
        sum=0
        for i in range(row):
            for j in range(row):
                if (i==j) or (i+j == row-1):
                    sum = sum + mat[i][j]
        return sum