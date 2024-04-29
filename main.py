from algorithms.matrix_addition_subtraction import SquareMatricesAdditionOrSubtraction
# from copy import deepcopy, copy
import math
from algorithms.matrix_padding import PowerOfTwoSquareMatrixPadding

# matrix1 = [[1, 2], [2, 3]]
# matrix2 = [[2, 3], [3, 5]]
# list1 = [1, 2, 3]
#
# list1_copy = list1.copy()
# list1_copy.append(1)
# print(list1_copy)
# print(list1)
#
# matrix1_copy = [x.copy() for x in matrix1]
#
# print(SquareMatricesAdditionOrSubtraction.add_or_subtract(matrix1_copy, matrix2, 2, 1))
# print(matrix1)
# print(matrix2)

matrix1 = [[1, 2], [2, 3]]
new_dim = 2 ** math.ceil(math.log2(5))
print(new_dim)
print(PowerOfTwoSquareMatrixPadding.pad_matrix(matrix1, new_dim))
