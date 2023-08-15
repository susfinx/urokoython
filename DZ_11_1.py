class Matrix:
    """класс Матрица"""
    def __init__(self, rows, cols):
        """создание матрицы"""
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        """строковое представление матрицы"""
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        """сравнение матрицы"""
        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True

    def __add__(self, other):
        """сложение"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матрицы должны совпадать для добавления")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other):
        """умножениe матрц"""
        if self.cols != other.rows:
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                result.data[i][j] = dot_product

        return result

if __name__=='__main__':

    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    print(matrix1)
    print(matrix2)
    print("Matrix 1 == Matrix 2:", matrix1 == matrix2)
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)
