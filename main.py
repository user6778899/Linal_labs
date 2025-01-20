class SparseMatrix:
    def __init__(self, n, m, grid=[]):
        self.n = n
        self.m = m
        self.rows = []
        self.cols = []
        self.values = []
        if grid != []:
            for i in range(n):
                self.add_row(grid[i], i)

    def add_row(self, row, row_index):
        for col_index, value in enumerate(row):
            if value != 0:
                self.rows.append(row_index)
                self.cols.append(col_index)
                self.values.append(value)

    def trace(self):
        trace_sum = 0
        for r, c, v in zip(self.rows, self.cols, self.values):
            if r == c:
                trace_sum += v
        return trace_sum

    def get_element(self, row_index, col_index, o=0):
        if o != 0:
            row_index, col_index = row_index - 1, col_index - 1
        for i in range(len(self.rows)):
            if self.rows[i] == row_index and self.cols[i] == col_index:
                return self.values[i]
        return 0

    def print_sparse(self): # выводит разряженную матрицу
        print(self.rows)
        print(self.cols)
        print(self.values)


    def __str__(self):
        full_matrix = [[0] * self.m for _ in range(self.n)]
        for i, j, value in zip(self.rows, self.cols, self.values):
            full_matrix[i][j] = value
        return '\n'.join(' '.join(map(str, row)) for row in full_matrix)


def print_grid(n, m, grid, k=3): # Выводит обычный вид матрицы
    for i in range(n):
        for j in range(m):
            tab = ' '*(k-len(str(grid[i][j])))
            print(grid[i][j], end=tab)
        print()


def sum_matrices(matrix1, matrix2):
    if matrix1.n != matrix2.n or matrix1.m != matrix2.m:
        print('Матрицы разного размера, их нельзя сложить!')
        return

    result = SparseMatrix(matrix1.n, matrix1.m)

    for r, c, v in zip(matrix1.rows, matrix1.cols, matrix1.values):
        result.rows.append(r)
        result.cols.append(c)
        result.values.append(v)

    for r, c, v in zip(matrix2.rows, matrix2.cols, matrix2.values):
        found = False
        for i in range(len(result.rows)):
            if result.rows[i] == r and result.cols[i] == c:
                result.values[i] += v
                found = True
                break
        if not found:
            result.rows.append(r)
            result.cols.append(c)
            result.values.append(v)

    return result


def multiply_int(matrix, scalar):
    result = SparseMatrix(matrix.n, matrix.m)
    for r, c, v in zip(matrix.rows, matrix.cols, matrix.values):
        result.rows.append(r)
        result.cols.append(c)
        result.values.append(v * scalar)
    return result


def multiply_matrices(matrix1, matrix2):
    if matrix1.m != matrix2.n:
        print('Матрицы разного размера, их нельзя перемножить!')
        return

    result = SparseMatrix(matrix1.n, matrix2.m)

    for i in range(matrix1.n):
        for j in range(matrix2.m):
            sum_value = 0
            for r1, c1, v1 in zip(matrix1.rows, matrix1.cols, matrix1.values):
                if r1 == i:
                    for r2, c2, v2 in zip(matrix2.rows, matrix2.cols, matrix2.values):
                        if c1 == r2 and c2 == j:
                            sum_value += v1 * v2
            if sum_value != 0:
                result.rows.append(i)
                result.cols.append(j)
                result.values.append(sum_value)

    return result



def get_minor(matrix, row, col):
    """
    Получение минора для разряженной матрицы (матрицы без строки `row` и столбца `col`).
    """
    minor = SparseMatrix(matrix.n - 1, matrix.m - 1)
    for i in range(matrix.n):
        if i == row:
            continue
        for j in range(matrix.m):
            if j == col:
                continue
            value = matrix.get_element(i, j)
            if value != 0:
                new_row = i if i < row else i - 1
                new_col = j if j < col else j - 1
                minor.add_row([value if x == new_col else 0 for x in range(minor.m)], new_row)
    return minor


def determinant(matrix):
    """
    Вычисление детерминанта для разряженной матрицы рекурсивно.
    """
    if matrix.n != matrix.m:
        raise ValueError("Матрица должна быть квадратной для вычисления детерминанта.")
    
    n = matrix.n
    if n == 1:
        return matrix.get_element(0, 0)
    if n == 2:
        a = matrix.get_element(0, 0)
        b = matrix.get_element(0, 1)
        c = matrix.get_element(1, 0)
        d = matrix.get_element(1, 1)
        return a * d - b * c
    
    det = 0
    for col in range(n):
        minor = get_minor(matrix, 0, col)
        det += ((-1) ** col) * matrix.get_element(0, col) * determinant(minor)
    
    return det


def exists_reverse(mat): # Существует ли обратная
    if determinant(mat) == 0:
        return 'Нет'
    else:
        return 'Да'


if __name__ == "__main__":
    print('|--------------------|')
    print('Задание 1')
    n, m = map(int, input("Введите размер матрицы N и M через пробел: ").split())
    matrix = SparseMatrix(n, m)

    print("Введите матрицу (через пробелы на каждой строке):")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.add_row(row, i)

    trace = matrix.trace()
    print(f"След матрицы: {trace}")

    i, j = map(int, input("Введите индексы для получения элемента матрицы (через пробел): ").split())
    element = matrix.get_element(i, j, 1)
    print(f"Элемент на позиции ({i}, {j}): {element}")


    print('|--------------------|')
    print('Задание 2')
    n1, m1 = map(int, input("Введите размер первой матрицы N1 и M1 через пробел: ").split())
    matrix1 = SparseMatrix(n1, m1)

    print("Введите первую матрицу (через пробелы на каждой строке):")
    for i in range(n1):
        row = list(map(float, input().split()))
        matrix1.add_row(row, i)

    n2, m2 = map(int, input("Введите размер второй матрицы N2 и M2 через пробел: ").split())
    matrix2 = SparseMatrix(n2, m2)

    print("Введите вторую матрицу (через пробелы на каждой строке):")
    for i in range(n2):
        row = list(map(float, input().split()))
        matrix2.add_row(row, i)

    print("Сложение матриц:")
    sum_result = sum_matrices(matrix1, matrix2)
    if sum_result:
        print(sum_result)

    scalar = float(input("Введите скаляр для умножения: "))
    print(f"Умножение первой матрицы на скаляр {scalar}:")
    scalar_result = multiply_int(matrix1, scalar)
    print(scalar_result)

    print("Умножение матриц:")
    multiplication_result = multiply_matrices(matrix1, matrix2)
    if multiplication_result:
        print(multiplication_result)


    print('|--------------------|')
    print('Задание 3')
    n = int(input("Введите размер матрицы (N): "))
    matrix = SparseMatrix(n, n)

    print("Введите матрицу:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.add_row(row, i)

    print(matrix)

    det = determinant(matrix)
    print("Определитель:", det)
    print(exists_reverse(matrix))
