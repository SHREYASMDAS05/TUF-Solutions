class Solution:
    def shortestDistance(self, matrix):
        row , col = len(matrix) , len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')

        for k in range(row):
            for i in range(row):
                for j in range(col):
                    matrix[i][j] = min(matrix[i][j] , matrix[i][k] + matrix[k][j])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1

        return matrix
    