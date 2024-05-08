from abc import ABC, abstractmethod
from threading import Thread


class ArraySorting(ABC):
    """
    Abstract base class for sorting algorithms.
    """
    @abstractmethod
    def sort(self, array: list[int | float | str]) -> None:
        """
        Abstract method that should be implemented by subclasses.
        Sorts the given number array in ascending order, and string array in alphabetical order.
        The original array is modified, and it should contain only integers/floats or only strings.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        pass


class AQuickSort(ArraySorting):
    """
    Abstract base class for quick sort algorithm.
    """
    def sort(self, array: list[int | float | str]) -> None:
        """
        Sorts the given number array in ascending order, and string array in alphabetical order
        using quick sort algorithm.
        The original array is modified, and it should contain only integers/floats or only strings.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        self.quick_sort(array, 0, len(array) - 1)

    @abstractmethod
    def quick_sort(self, array: list[int | float | str], beg: int, end: int) -> None:
        """
        Abstract method that should be implemented by subclasses.
        Sorts the given array using the quick sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]
        :param beg: The beginning index of the array.
        :type beg: int
        :param end: The ending index of the array.
        :type end: int

        :return: None
        """
        pass

    def _partition(self, array: list[int | float | str], beg: int, end: int) -> int:
        """
        Partitions the array by the last element(pivot). Elements that are 'greater' than the pivot are placed to
        the right of the pivot, while other elements are placed to the left of the pivot in the array.

        :param array: The array to be partitioned.
        :type array: list[int | float | str]
        :param beg: The beginning index of the array.
        :type beg: int
        :param end: The ending index of the array.
        :type end: int

        :return: The index of the pivot element in array.
        :rtype: int
        """
        pivot = array[end]
        index = beg

        for i in range(beg, end):
            if array[i] <= pivot:
                array[i], array[index] = array[index], array[i]
                index += 1

        array[index], array[end] = array[end], array[index]

        return index


# Time Complexity O(n*log_n)
class QuickSort(AQuickSort):
    def quick_sort(self, array: list[int | float | str], beg: int, end: int) -> None:
        """
        Sorts the given array using the sequential version of quick sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]
        :param beg: The beginning index of the array.
        :type beg: int
        :param end: The ending index of the array.
        :type end: int

        :return: None
        """
        if beg <= end:
            pivot_index = self._partition(array, beg, end)
            self.quick_sort(array, beg, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, end)


class MultithreadingQuickSort(AQuickSort):
    # def __init__(self):
    #     self._quick_sorting = QuickSort()

    def quick_sort(self, array: list[int | float | str], beg: int, end: int) -> None:
        """
        Sorts the given array using the multithreading version of quick sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]
        :param beg: The beginning index of the array.
        :type beg: int
        :param end: The ending index of the array.
        :type end: int

        :return: None
        """
        if beg <= end:
            pivot_index = self._partition(array, beg, end)

            th_1 = Thread(target=self.quick_sort, args=(array, beg, pivot_index - 1))
            th_2 = Thread(target=self.quick_sort, args=(array, pivot_index + 1, end))

            th_1.start()
            th_2.start()

            th_1.join()
            th_2.join()


class AMergeSort(ArraySorting):
    """
    Abstract base class for merge sort algorithm.
    """
    def sort(self, array: list[int | float | str]) -> None:
        """
        Sorts the given number array in ascending order, and string array in alphabetical order
        using quick sort algorithm.
        The original array is modified, and it should contain only integers/floats or only strings.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        self.merge_sort(array)

    @abstractmethod
    def merge_sort(self, array: list[int | float | str]):
        """
        Abstract method that should be implemented by subclasses.
        Sorts the given array using the merge sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        pass

    def _merge(self, array: list[int | float | str], left: list[int | float | str], right: list[int | float | str])\
            -> None:
        """
        Merges two subarrays into a single sorted array.
        Modifies the original array by merging the two subarrays in sorted order.

        :param array: The original array containing two subarrays.
        :type array: list[int | float | str]
        :param left: The left subarray to be merged.
        :type left: list[int | float | str]
        :param right: The right subarray to be merged.
        :type right: list[int | float | str]

        :return: None
        """
        left_i, right_i, arr_i = 0, 0, 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                array[arr_i] = left[left_i]
                left_i += 1
                arr_i += 1
            else:
                array[arr_i] = right[right_i]
                right_i += 1
                arr_i += 1

        while left_i < len(left):
            array[arr_i] = left[left_i]
            arr_i += 1
            left_i += 1

        while right_i < len(right):
            array[arr_i] = right[right_i]
            arr_i += 1
            right_i += 1


# Time Complexity O(n*log_n)
class MergeSort(AMergeSort):
    def merge_sort(self, array: list[int | float | str]):
        """
        Sorts the given array using the sequential version of quick sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        self._merge(array, left, right)


class MultithreadingMergeSort(AMergeSort):
    # def __init__(self):
    #     self._merge_sorting = MergeSort()

    def merge_sort(self, array: list[int | float | str]):
        """
        Sorts the given array using the multithreading version of merge sort algorithm.

        :param array: The array to be sorted.
        :type array: list[int | float | str]

        :return: None
        """
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        th_1 = Thread(target=self.merge_sort, args=(left,))
        th_2 = Thread(target=self.merge_sort, args=(right,))

        th_1.start()
        th_2.start()

        th_1.join()
        th_2.join()

        self._merge(array, left, right)
