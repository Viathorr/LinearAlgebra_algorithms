from .array_sorting import ArraySorting
import time


class ExecutionTimeDecorator(ArraySorting):
    """
    A decorator class that adds functionality to measure the execution time of the sorting algorithm.
    This class wraps an instance of a class that implements the ArraySorting interface and adds
    functionality to measure the execution time of the sorting algorithm.
    """
    def __init__(self, sorting: ArraySorting) -> None:
        """
        Initializes the ExecutionTimeDecorator.

        :param sorting: An instance of a class that implements the ArraySorting interface.
        :type sorting: ArraySorting
        """
        self.__sorting = sorting

    def sort(self, array: list[int | float | str]) -> None:
        """
        Sorts the given number array in ascending order, and string array in alphabetical order,
        using the wrapped sorting algorithm and prints the execution time of the sorting algorithm.
        The original array is modified, and it should contain only integers/floats or only strings.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        start = time.time()
        self.__sorting.sort(array)
        print(f'Algorithm execution time: {time.time() - start:.6f}s')
