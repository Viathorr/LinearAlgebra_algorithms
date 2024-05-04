from abc import ABC, abstractmethod


class MatrixPadding(ABC):
    @staticmethod
    @abstractmethod
    def pad_matrix(matrix: list[list[int | float]], new_dim: int) -> list[list[int | float]]:
        pass


class PowerOfTwoSquareMatrixPadding(MatrixPadding):
    @staticmethod
    def pad_matrix(matrix: list[list[int | float]], new_dim: int) -> list[list[int | float]]:
        n, m = len(matrix), len(matrix[0])
        padded_matrix = [[0] * new_dim for _ in range(new_dim)]
        for i in range(n):
            for j in range(m):
                padded_matrix[i][j] = matrix[i][j]

        return padded_matrix
