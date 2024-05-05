from .array_sorting import ArraySorting
import time


class ExecutionTimeDecorator(ArraySorting):
    def __init__(self, alg: ArraySorting):
        self.__algorithm = alg

    def sort(self, array: list[int | float | str]) -> None:
        start = time.time()
        self.__algorithm.sort(array)
        print(f'Sorting execution time: {time.time() - start:.6f}s')