from abc import ABC, abstractmethod
import time
import math
from matrix_addition_subtraction import SquareMatricesAdditionOrSubtraction
from matrix_padding import PowerOfTwoSquareMatrixPadding


def print_matrix(matrix: list[list[int | float]]):
    for row in matrix:
        print(row)


class MatrixMultiplication(ABC):
    def execute(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> list[list[int | float]]:
        if self.__can_multiply(matrix1, matrix2):
            return self._multiply(matrix1, matrix2)
        else:
            raise Exception('Matrices with provided dimensions can\'t be multiplied: The number of columns in first'
                            'matrix is not equal to the number of rows in second matrix.')

    @abstractmethod
    def _multiply(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> list[list[int | float]]:
        pass

    def __can_multiply(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> bool:
        if len(matrix1) and len(matrix2) and len(matrix1[0]) == len(matrix2):
            return True
        else:
            return False


# Decorator pattern (adds execution time counting and displaying)
class TimeMatrixMultiplication(MatrixMultiplication):
    def __init__(self, matrix_multiplication: MatrixMultiplication):
        self._matrix_multiplication = matrix_multiplication

    def _multiply(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> list[list[int | float]]:
        start = time.time()
        res = self._matrix_multiplication._multiply(matrix1, matrix2)
        print(f'Multiplication execution time: {time.time() - start:.6f}s')
        return res


# Time Complexity: O(n^3)
class NaiveMatrixMultiplication(MatrixMultiplication):
    def _multiply(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> list[list[int | float]]:
        rows_1, rows_2, cols_1, cols_2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])

        res_matrix = [[0 for _ in range(cols_2)] for _ in range(rows_1)]

        for i in range(rows_1):
            for j in range(cols_2):
                for k in range(cols_1):
                    res_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

        return res_matrix


# Time Complexity: O(n^2.8074)
class StrassenMatrixMultiplication(MatrixMultiplication):
    def _multiply(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]]) -> list[list[int | float]]:
        rows_1, cols_1, cols_2 = len(matrix1), len(matrix1[0]), len(matrix2[0])
        max_dim = max([rows_1, cols_1, cols_2])
        new_dim = 2 ** math.ceil(math.log2(max_dim))
        matrix1 = PowerOfTwoSquareMatrixPadding.pad_matrix(matrix1, new_dim)
        matrix2 = PowerOfTwoSquareMatrixPadding.pad_matrix(matrix2, new_dim)
        start = time.time()
        res_matrix = self.__strassen_algorithm(matrix1, matrix2, new_dim)
        end = time.time()
        print(f'Time: {end - start:.6f} seconds')
        return [[res_matrix[i][j] for j in range(cols_2)] for i in range(rows_1)]

    def __strassen_algorithm(self, matrix1: list[list[int | float]], matrix2: list[list[int | float]],
                             n: int) -> list[list[int | float]]:
        res_matrix = [[0] * n for _ in range(n)]

        if n == 1:
            res_matrix[0][0] = matrix1[0][0] * matrix2[0][0]
        else:
            split_index = n // 2  # n is always a power of 2

            a11, a12, a21, a22 = self.__split_matrix(matrix1, split_index)
            b11, b12, b21, b22 = self.__split_matrix(matrix2, split_index)

            # (A11 + A22) * (B11 + B22)
            m1 = self.__strassen_algorithm(SquareMatricesAdditionOrSubtraction.add_or_subtract(a11, a22, split_index),
                                           SquareMatricesAdditionOrSubtraction.add_or_subtract(b11, b22, split_index),
                                           split_index)
            # (A21 + A22) * B11
            m2 = self.__strassen_algorithm(SquareMatricesAdditionOrSubtraction.add_or_subtract(a21, a22, split_index),
                                           b11, split_index)
            # A11 * (B12 - B22)
            m3 = self.__strassen_algorithm(a11, SquareMatricesAdditionOrSubtraction.add_or_subtract(b12, b22,
                                                                                                    split_index, -1),
                                           split_index)
            # A22 * (B21 - B11)
            m4 = self.__strassen_algorithm(a22, SquareMatricesAdditionOrSubtraction.add_or_subtract(b21, b11,
                                                                                                    split_index, -1),
                                           split_index)
            # (A11 + A12) * B22
            m5 = self.__strassen_algorithm(SquareMatricesAdditionOrSubtraction.add_or_subtract(a11, a12, split_index),
                                           b22, split_index)
            # (A21 - A11) * (B11 + B12)
            m6 = self.__strassen_algorithm(SquareMatricesAdditionOrSubtraction.add_or_subtract(a21, a11, split_index,
                                                                                               -1),
                                           SquareMatricesAdditionOrSubtraction.add_or_subtract(b11, b12, split_index),
                                           split_index)
            # (A12 - A22) * (B21 + B22)
            m7 = self.__strassen_algorithm(SquareMatricesAdditionOrSubtraction.add_or_subtract(a12, a22, split_index,
                                                                                               -1),
                                           SquareMatricesAdditionOrSubtraction.add_or_subtract(b21, b22, split_index),
                                           split_index)

            # ((M1 + M4) - M5) + M7
            c11 = SquareMatricesAdditionOrSubtraction.add_or_subtract(
                    SquareMatricesAdditionOrSubtraction.add_or_subtract(
                        SquareMatricesAdditionOrSubtraction.add_or_subtract(m1, m4, split_index), m5, split_index, -1),
                    m7, split_index)
            # M3 + M5
            c12 = SquareMatricesAdditionOrSubtraction.add_or_subtract(m3, m5, split_index)
            # M2 + M4
            c21 = SquareMatricesAdditionOrSubtraction.add_or_subtract(m2, m4, split_index)
            # ((M1 - M2) + M3) + M6
            c22 = SquareMatricesAdditionOrSubtraction.add_or_subtract(
                    SquareMatricesAdditionOrSubtraction.add_or_subtract(
                        SquareMatricesAdditionOrSubtraction.add_or_subtract(m1, m2, split_index, -1), m3, split_index),
                    m6, split_index)

            for i in range(split_index):
                for j in range(split_index):
                    res_matrix[i][j] = c11[i][j]
                    res_matrix[i][j + split_index] = c12[i][j]
                    res_matrix[i + split_index][j] = c21[i][j]
                    res_matrix[i + split_index][j + split_index] = c22[i][j]

        return res_matrix

    def __split_matrix(self, matrix: list[list[int | float]], split_index: int):
        a11 = PowerOfTwoSquareMatrixPadding.pad_matrix([[]], split_index)
        a12 = PowerOfTwoSquareMatrixPadding.pad_matrix([[]], split_index)
        a21 = PowerOfTwoSquareMatrixPadding.pad_matrix([[]], split_index)
        a22 = PowerOfTwoSquareMatrixPadding.pad_matrix([[]], split_index)

        for i in range(split_index):
            for j in range(split_index):
                a11[i][j] = matrix[i][j]
                a12[i][j] = matrix[i][j + split_index]
                a21[i][j] = matrix[i + split_index][j]
                a22[i][j] = matrix[i + split_index][j + split_index]
        return a11, a12, a21, a22


if __name__ == "__main__":
    matrix_a = [[46, 12] * 3 for _ in range(6)]
    matrix_b = [[74, 38] * 3 for _ in range(6)]

    # dummy_matrix = [[1, 2, 3, 0, 0], [3, 4, 5, 0, 0], [0, 0, 0, 0, 0]]
    # rows1, cols2 = 2, 3
    # print([[dummy_matrix[i][j] for j in range(cols2)] for i in range(rows1)])

    multiplication = NaiveMatrixMultiplication()
    multiplication_with_exec_time = TimeMatrixMultiplication(multiplication)
    start_time = time.time()
    multiple_matrix = [[]]
    try:
        multiple_matrix = multiplication_with_exec_time.execute(matrix_a, matrix_b)
    except Exception as err:
        print(f'Error: \n{err.args[0]}')
    else:
        print(f"Multiple of two matrices: {multiple_matrix}, Time: {time.time() - start_time:.6f} seconds")
        print(f'size: {len(multiple_matrix)} x {len(multiple_matrix[0])}')

    # multiplication = StrassenMatrixMultiplication()
    # start_time = time.time()
    # multiple_matrix2 = multiplication.multiply(matrix_a, matrix_b)
    # end_time = time.time()
    # print(f"Multiple of two matrices: {multiple_matrix2}, Time: {end_time - start_time:.6f} seconds")
    # print(f'size: {len(multiple_matrix2)} x {len(multiple_matrix2[0])}')
