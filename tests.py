from main import *


print('Тесты к 1 заданию:')

n = 3
m = 3
grid = [
    [1, 0, 1],
    [2, 0, 4],
    [0, 0, 3]]
print('Изначальная матрица 1:')
for i in range(n):
    for j in range(m):
        tab = ' '*(3-len(str(grid[i][j])))
        print(grid[i][j], end=tab)
    print()
print('Разряженная матрица:')
mat = matrix(n, m, grid)
mat.print_sparse()
print('след матрицы: ', end='')
print(mat.trace())
print('Элемент (1, 2): ', end='')
print(mat.get_element(1, 2))
print('Элемент (2, 1): ', end='')
print(mat.get_element(2, 1))
print('Элемент (3, 3): ', end='')
print(mat.get_element(3, 3))
print()


n = 5
m = 5
grid = [
    [1, 0, 1, 0, 3],
    [2, 0, 4, -3, 0],
    [0, 0, 3, 9, 9],
    [2, 0, 0, -7, 0],
    [0, -5, 4, 0, 0]]
print('Изначальная матрица 2:')
for i in range(n):
    for j in range(m):
        tab = ' '*(3-len(str(grid[i][j])))
        print(grid[i][j], end=tab)
    print()
print('Разряженная матрица:')
mat = matrix(n, m, grid)
mat.print_sparse()
print('след матрицы: ', end='')
print(mat.trace())
print('Элемент (1, 2): ', end='')
print(mat.get_element(1, 2))
print('Элемент (5, 3): ', end='')
print(mat.get_element(5, 3))
print('Элемент (3, 4): ', end='')
print(mat.get_element(3, 4))
print()
print()


print('Тесты ко 2 заданию:')
n1 = 2
m1 = 3
grid1 = [
    [1, -1, 0],
    [0, 1, 0]]
mat1 = matrix(n1, m1, grid1)
n2 = 2
m2 = 3
grid2 = [
    [9, 1, 9],
    [-1, 0, -9]]
mat2 = matrix(n2, m2, grid2)

print('Матрица 1:')
print_grid(n1, m1, grid1)
print('разряженный вид:')
mat1.print_sparse()

print('Матрица 2:')
print_grid(n2, m2, grid2)
print('разряженный вид:')
mat2.print_sparse()

mat_sum = sum_matrices(mat1, mat2)
print('разряженный вид суммы:')
mat_sum.print_sparse()
print('обычный вид суммы:')
print_mat(mat_sum)
print('Умножение матрицы суммы на 0.2:')
mat_mult = multiply_int(mat_sum, 0.2)
print_mat(mat_mult, k=5)
print('Перемножение матриц:')
mat_mult2 = multiply_matrices(mat1, mat2)
if mat_mult2:
    print_mat(mat_mult2)
    print('разряженный вид:')
    mat_mult2.print_sparse()
print()

n1 = 4
m1 = 4
grid1 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]]
mat1 = matrix(n1, m1, grid1)
n2 = 4
m2 = 4
grid2 = [
    [0, 8, -3, 2],
    [0, 2, 0, 4],
    [1, 0, 0, 0],
    [0, 3, 0, -1]]
mat2 = matrix(n2, m2, grid2)

print('Матрица 1:')
print_grid(n1, m1, grid1)
print('разряженный вид:')
mat1.print_sparse()

print('Матрица 2:')
print_grid(n2, m2, grid2)
print('разряженный вид:')
mat2.print_sparse()

mat_sum = sum_matrices(mat1, mat2)
print('разряженный вид суммы:')
mat_sum.print_sparse()
print('обычный вид суммы:')
print_mat(mat_sum)
print('Умножение матрицы суммы на -1:')
mat_mult = multiply_int(mat_sum, -1)
print_mat(mat_mult)
print('Перемножение матриц:')
mat_mult2 = multiply_matrices(mat1, mat2)
print_mat(mat_mult2)
print('разряженный вид:')
mat_mult2.print_sparse()
print()
print()


print('Тесты к 3 заданию:')
n = 2
m = 2
grid = [
    [1, -1],
    [0, 1]]
mat = matrix(n, m, grid)
print('Матрица:')
print_grid(n, m, grid)
print('разряженный вид:')
mat.print_sparse()
print('Определитель = ', end='')
det = determinant(mat)
print(det)
print('“Существует ли матрица, обратная данной?”')
print(exists_reverse(mat))
print()

n = 5
m = 5
grid = [
    [1, 0, 1, 0, 3],
    [2, 0, 4, -3, 0],
    [0, 0, 3, 9, 9],
    [2, 0, 0, -7, 0],
    [0, -5, 4, 0, 0]]
mat = matrix(n, m, grid)
print('Изначальная матрица 2:')
print_grid(n, m, grid)
print('разряженный вид:')
mat.print_sparse()
print('Определитель = ', end='')
det = determinant(mat)
print(det)
print('“Существует ли матрица, обратная данной?”')
print(exists_reverse(mat))
print()
