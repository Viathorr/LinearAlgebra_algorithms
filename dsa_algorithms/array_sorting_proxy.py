from .array_sorting import *


class ArraySortingProxy(ArraySorting):
    """
    Proxy class for sorting arrays, ensuring array validity before sorting.
    This class acts as a proxy to prevent execution of sorting operation by other sorting classes if the array contains
    elements other than only integers/floats, or only strings.
    """
    def __init__(self, sorting: ArraySorting) -> None:
        """
        Initializes the ArraySortingProxy.

        :param sorting: An instance of a class that implements the ArraySorting interface.
        :type sorting: ArraySorting
        """
        self.__sorting = sorting

    def sort(self, array: list[int | float | str]) -> None:
        """
        Sorts the given number array in ascending order, and string array in alphabetical order,
        after validating the array content.
        The original array is modified, and it should contain only integers/floats or only strings.

        :param array: The array to be sorted.
        :type array: list[int | float | str]
        :raises TypeError: If the array contains elements other than integers, floats, or strings.

        :return: None
        """
        if self.__check_array_type(array):
            self.__sorting.sort(array)
        else:
            raise TypeError('Array should contain only int, float or str types.')

    def __check_array_type(self, array: list) -> bool:
        """
        Checks if the array contains only integers/floats, or only strings.

        :param array: The array to check.
        :type array: list

        :return: True if the array contains only integers, floats, or strings, False otherwise.
        :rtype: bool
        """
        return all(isinstance(x, (int, float)) for x in array) or all(isinstance(x, str) for x in array)
