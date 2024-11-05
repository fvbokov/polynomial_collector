import copy

class SquareMatrix:
    n = 0
    data = []
    
    def __init__(self, n, data=0):
        self.n = n
        if data == 0:
            self.data = list()
            for i in range(n):
                self.data.append([])
                for j in range(n):
                    self.data[i].append(0)
        else:
            self.data = copy.deepcopy(data)

    def __str__(self):
        rslt = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                rslt += f"{self.data[i][j]} "
            rslt += '\n'
        return rslt
    
    @staticmethod
    def id_matrix(n):
        matrix = SquareMatrix(n, 0)
        matrix.data = list()
        for i in range(n):
            matrix.data.append([])
            for j in range(n):
                if i == j:
                    matrix.data[i].append(1)
                else:
                    matrix.data[i].append(0)
        return matrix

    @staticmethod
    def multiply(left, right):
        rslt = SquareMatrix(left.n, 0)
        for i in range(left.n):
            for j in range(left.n):
                for k in range(left.n):
                    rslt.data[i][j] += left.data[i][k] * right.data[k][j]
        return rslt
    
    @staticmethod
    def add(left, right):
        rslt = SquareMatrix(left.n, 0)
        for i in range(left.n):
            for j in range(left.n):
                rslt.data[i][j] = left.data[i][j] + right.data[i][j]
        return rslt
    
    @staticmethod
    def raise_to_a_power(matrix, n):
        if n == 0:
            return SquareMatrix.id_matrix(matrix.n)

        rslt = copy.deepcopy(matrix)
        for i in range(1, n):
            rslt = SquareMatrix.multiply(rslt, matrix)
        return rslt
      
    @staticmethod
    def multiply_by_a_number(matrix, n):
        rslt = SquareMatrix(matrix.n, 0)
        for i in range(matrix.n):
            for j in range(matrix.n):
                for k in range(matrix.n):
                    rslt.data[i][j] = matrix.data[i][j] * n
        return rslt