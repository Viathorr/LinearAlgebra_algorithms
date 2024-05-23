from abc import ABC, abstractmethod
from .matrix_multiplication import NaiveMatrixMultiplication
from copy import deepcopy


class MatrixInverse(ABC):
    @abstractmethod
    def inverse(self, matrix: list[list[int | float]]) -> list[list[int | float]]:
        pass


class ValidatedMatrixInverse(MatrixInverse):
    def __init__(self, matrix_inverse: MatrixInverse):
        self._matrix_inverse = matrix_inverse

    def inverse(self, matrix: list[list[int | float]]) -> list[list[int | float]]:
        if self.__inverse_exists(matrix):
            return self._matrix_inverse.inverse(matrix)
        else:
            raise Exception('Matrix doesn\'t have inverse. It is either non-square or '
                            'determinant of matrix is equal to 0.')

    def __inverse_exists(self, matrix: list[list[int | float]]) -> bool:
        # TODO implement when Determinant class is ready
        pass  # if matrix is square and det(matrix) != 0 return true


class MatrixInverseByGaussJordanElimination(MatrixInverse):
    def inverse(self, matrix: list[list[int | float]]) -> list[list[int | float]]:
        dim = len(matrix)

        for i in range(dim):
            for j in range(dim):
                if i == j:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)

        for i in range(dim - 1, 0, -1):
            if matrix[i - 1][0] < matrix[i][0]:
                temp_arr = matrix[i]
                matrix[i] = matrix[i - 1]
                matrix[i - 1] = temp_arr

        for row in matrix:
            print(row)

        for i in range(dim):
            for j in range(dim):
                if j != i:
                    temp = matrix[j][i] / matrix[i][i]
                    for k in range(2 * dim):
                        matrix[j][k] -= matrix[i][k] * temp

        for i in range(dim):
            temp = matrix[i][i]
            for j in range(2 * dim):
                matrix[i][j] = matrix[i][j] / temp

        for i in range(dim):
            print('[ ', end='')
            for j in range(dim):
                print(f'{matrix[i][j + dim]:.2f}', end=' ')
            print(']')

        return [row[dim:] for row in matrix]


# TODO implement when Determinant class is ready
class MatrixInverseByMinors(MatrixInverse):
    def inverse(self, matrix: list[list[int | float]]) -> list[list[int | float]]:
        pass


if __name__ == '__main__':
    m = [[4, 3, 5, 3], [3, 2, 9, 2], [3, 7, 2, 4], [5, -1, 2, -5]]
    compute_inverse = MatrixInverseByGaussJordanElimination()
    compute_multiple = NaiveMatrixMultiplication()

    inverse = compute_inverse.inverse(deepcopy(m))

    multiple = compute_multiple._multiply(m, inverse)

    for i in multiple:
        print('[ ', end='')
        for j in i:
            print(f'{j:.2f}', end=' ')
        print(']')
