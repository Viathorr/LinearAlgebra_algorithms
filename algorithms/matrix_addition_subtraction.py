class SquareMatricesAdditionOrSubtraction:
    @staticmethod
    # multiplier is equal to 1 if we add matrix, and it is equal to -1 if we subtract matrix
    # by default 1
    # it is expected, that matrices are passed by value not by reference
    def add_or_subtract(matrix1: list[list[int | float]], matrix2: list[list[int | float]], size: int,
                        multiplier: int = 1) -> list[list[int | float]]:
        matrix1_copy = [row.copy() for row in matrix1]
        for i in range(size):
            for j in range(size):
                matrix1_copy[i][j] += multiplier * matrix2[i][j]

        return matrix1_copy
