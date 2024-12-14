class matrix:
    def __init__(self, n, m, grid, flag=True):
        self.n = n
        self.m = m
        
        # Разряженный вид матрицы
        if flag:
            self.sparse_grid = self.sparse(grid) # Перевод из обычной в разряженную
        else:
            self.sparse_grid = grid # Если на входе уже разряженная
        

    def sparse(self, grid): # Создаёт разряженную матрицу
        sparse_grid = {}
        for i in range(self.n): 
            for j in range(self.m): 
                if grid[i][j] != 0: 
                    sparse_grid[(i, j)] = grid[i][j]
                else:
                    continue
        return sparse_grid


    def print_sparse(self): # Выводит словарь с разряженной матрицей
        print(self.sparse_grid)
        

    def trace(self): # След матрицы
        if self.n != self.m: # Проверка на квадртность
            print('Матрица не квадратная!')
            return 0
        s = 0 
        for i in range(self.n):
            if self.sparse_grid.get((i, i)):
                s += self.sparse_grid[(i, i)] 
        return s
    

    def get_element(self, i, j): # Возврат элемента по индексу и столбцу
        if self.sparse_grid.get((i-1, j-1)):
            return self.sparse_grid[(i-1, j-1)]
        else:
            return 0


def print_grid(n, m, grid, k=3): # Выводит обычный вид матрицы
    for i in range(n):
        for j in range(m):
            tab = ' '*(k-len(str(grid[i][j])))
            print(grid[i][j], end=tab)
        print()


def print_mat(mat, k=3): # По экземпляру класса выводит матрицу в обычном виде
    for i in range(mat.n):
        for j in range(mat.m):
            if mat.sparse_grid.get((i, j)):
                tab = ' '*(k-len(str(mat.sparse_grid[(i, j)])))
                print(mat.sparse_grid[(i, j)], end=tab)
            else:
                print(0, end='  ')
        print()

        
def sum_matrices(mat1, mat2): # Сложение матриц
    if mat1.n != mat2.n or mat1.m != mat2.m:
        print('Матрицы разного размера, их нельзя сложить!')
        return 0
    zero_list = [] # для удаления нулевых элементов
    sparse_grid_copy = mat1.sparse_grid.copy() # копируем словарь
    mat_sum = matrix(mat1.n, mat1.m, sparse_grid_copy, flag=False)
    # Прибавляем элементы из 2 матрицы в sum матрицу
    for i in mat2.sparse_grid:
        if mat_sum.sparse_grid.get(i):
            mat_sum.sparse_grid[i] += mat2.sparse_grid[i]
            if mat_sum.sparse_grid[i] == 0:
                zero_list.append(i)
        else:
            mat_sum.sparse_grid[i] = mat2.sparse_grid[i]
    for i in zero_list:
        del mat_sum.sparse_grid[i]
    return mat_sum
    


def multiply_int(mat, x): # Умножение матрицы на число
    sparse_grid_copy = mat.sparse_grid.copy()
    mat_mult = matrix(mat.n, mat.m, sparse_grid_copy, flag=False)
    zero_list = []
    for i in mat_mult.sparse_grid:
        mat_mult.sparse_grid[i] *= x
        if mat_mult.sparse_grid[i] == 0:
            zero_list.append(i)
    for i in zero_list:
        del mat_mult.sparse_grid[i]
    return mat_mult
    

def multiply_matrices(mat1, mat2): # Перемножение матриц
    if mat1.m != mat2.n:
        print('Матрицы разного размера, их нельзя перемножить!')
        return 0
    mat_mult = matrix(mat1.n, mat1.m, {}, flag=False)
    for i in range(mat1.n): 
        for j in range(mat2.m):
            summ = 0
            for k in range(mat1.m): 
                summ += mat1.get_element(i+1, k+1) * mat2.get_element(k+1, j+1)
            if summ != 0:
                mat_mult.sparse_grid[(i, j)] = summ
    return mat_mult 


def minor(mat, i, j): # Подсчёт минора
        minor_sum = []
        for k in range(mat.n):
            if k == i: continue
            minor_row = []
            for l in range(mat.m):
                if l == j: continue
                minor_row.append(mat.get_element(k+1, l+1))
            minor_sum.append(minor_row)
        mat2 = matrix(mat.n-1, mat.m-1, minor_sum)
        return mat2

    
def determinant(mat):  # Определитель
    if mat.n != mat.m:
        print('Матрицa неправильного размера, не квадратная!')
        return 0
    if mat.n == 1: # для маленьких входных матриц
        a = mat.get_element(0+1, 0+1)
        return a
    if mat.n == 2: # последний шаг
        a = mat.get_element(0+1, 0+1)
        b = mat.get_element(0+1, 1+1)
        c = mat.get_element(1+1, 0+1)
        d = mat.get_element(1+1, 1+1) 
        return a*d-b*c 

    det = 0
    for i in range(mat.m):
        det += ((-1)**i) * mat.get_element(1, i+1) * determinant(minor(mat, 0, i)) # формула
    return det


def exists_reverse(mat): # Существует ли обратная
    if determinant(mat) == 0:
        return 'Нет'
    else:
        return 'Да'


if __name__ == "__main__":
    mat = matrix(3, 3, [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
    ])

    # Вывод матрицы и следа
    print("Матрица:")
    print_mat(mat)
    print("След матрицы:", mat.trace())

    print('|'+'-'*20+'|')

    # Матрица A
    matrix_a = matrix(2, 2, [
        [1, 2],
        [3, 4]
    ])
    
    # Матрица B
    matrix_b = matrix(2, 2, [
        [5, 6],
        [7, 8]
    ])
    
    # Сложение
    result = sum_matrices(matrix_a, matrix_b)
    print("Результат сложения:")
    print_mat(result)

    print('|'+'-'*20+'|')

    # Матрица 3x3
    mat = matrix(3, 3, [
        [2, -1, 0],
        [1, 3, 2],
        [0, -2, 1]
    ])

    # Вычисление определителя
    det = determinant(mat)
    print("Определитель:", det)
    print("Обратима ли матрица:", "да" if det != 0 else "нет")
