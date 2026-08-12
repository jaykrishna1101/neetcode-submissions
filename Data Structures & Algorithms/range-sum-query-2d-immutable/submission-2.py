class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sm = [[0 for _ in range(n)] for _ in range(m)]
        print(self.sm)
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        self.sm[i][j] = matrix[i][j]
                        # print(sm[0][0])
                    else:
                        self.sm[i][j] = self.sm[i][j-1] + matrix[i][j]
                        # print(sm[0][0])
                elif j == 0:

                    self.sm[i][j] = self.sm[i-1][j] + matrix[i][j]
                    # print(sm[0][0])
                else:
                    self.sm[i][j] = self.sm[i-1][j] + self.sm[i][j-1] - self.sm[i-1][j-1] + matrix[i][j]
                    # print(sm[0][0])
        print(self.sm)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            if col1 == 0:
                # print(self.sm[row2][col2])
                return self.sm[row2][col2]
            else:
                return self.sm[row2][col2] - self.sm[row2][col1-1]
        elif col1 == 0:
            return self.sm[row2][col2] - self.sm[row1-1][col2]
        else:
            # print(self.sm[row2][col2], self.sm[row1-1][col2], self.sm[row2][col1-1] , self.sm[row1-1][col1-1])
            return self.sm[row2][col2] - self.sm[row1-1][col2] - self.sm[row2][col1-1] + self.sm[row1-1][col1-1]
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)