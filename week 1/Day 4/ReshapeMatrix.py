class Solution(object):
    def matrixReshape(self, mat, r, c):
        row = len(mat)
        column = len(mat[0])
        OneD = []
        if r*c != row * column:
            return mat
        for i in range (row):
            for j in range(column):
                OneD.append(mat[i][j])
        mat1 = []
        pointer = 0
        for i in range (r):
            temp = []
            for j in range(c):
                temp.append(OneD[pointer])
                pointer +=1
            mat1.append(temp)
        return mat1