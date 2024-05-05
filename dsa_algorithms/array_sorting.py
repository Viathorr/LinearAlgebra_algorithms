from abc import ABC, abstractmethod
import time
from threading import Thread


class ArraySorting(ABC):
    @abstractmethod
    # Array is passed by ref, so it is changed automatically
    # Number arrays are sorted in ascending order
    # String arrays are sorted in alphabetical order
    def sort(self, array: list[int | float | str]) -> None:
        pass


class ExecutionTimeDecorator(ArraySorting):
    def __init__(self, alg: ArraySorting):
        self.__algorithm = alg

    def sort(self, array: list[int | float | str]) -> None:
        start = time.time()
        self.__algorithm.sort(array)
        print(f'Sorting execution time: {time.time() - start:.6f}s')


class ArraySortingProxy(ArraySorting):
    def __init__(self, sorting: ArraySorting):
        self._sorting = sorting

    def sort(self, array: list[int | float | str]) -> None:
        if self.__check_array_type(array):
            self._sorting.sort(array)
        else:
            raise TypeError('Array should contain only int, float or str types.')

    def __check_array_type(self, array: list):
        return all(isinstance(x, int) for x in array) or all(isinstance(x, float) for x in array) or \
               all(isinstance(x, str) for x in array)


class AQuickSort(ArraySorting):
    def sort(self, array: list[int | float | str]) -> None:
        self.quick_sort(array, 0, len(array) - 1)

    @abstractmethod
    def quick_sort(self, array: list[int | float | str], beg: int, end: int) -> None:
        pass

    def _partition(self, array: list[int | float | str], beg: int, end: int) -> int:
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
        if beg <= end:
            pivot_index = self._partition(array, beg, end)
            self.quick_sort(array, beg, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, end)


class MultithreadingQuickSort(AQuickSort):
    def __init__(self):
        self._quick_sorting = QuickSort()

    def quick_sort(self, array: list[int | float | str], beg: int, end: int) -> None:
        if beg <= end:
            pivot_index = self._partition(array, beg, end)

            th_1 = Thread(target=self._quick_sorting.quick_sort, args=(array, beg, pivot_index - 1))
            th_2 = Thread(target=self._quick_sorting.quick_sort, args=(array, pivot_index + 1, end))

            th_1.start()
            th_2.start()

            th_1.join()
            th_2.join()


class AMergeSort(ArraySorting):
    def sort(self, array: list[int | float | str]) -> None:
        self.merge_sort(array)

    @abstractmethod
    def merge_sort(self, array: list[int | float | str]):
        pass

    def _merge(self, array: list[int | float | str], left: list[int | float | str], right: list[int | float | str]):
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
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        self._merge(array, left, right)


class MultithreadingMergeSort(AMergeSort):
    def __init__(self):
        self._merge_sorting = MergeSort()

    def merge_sort(self, array: list[int | float | str]):
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        th_1 = Thread(target=self._merge_sorting.merge_sort, args=(left,))
        th_2 = Thread(target=self._merge_sorting.merge_sort, args=(right,))

        th_1.start()
        th_2.start()

        th_1.join()
        th_2.join()

        self._merge(array, left, right)


def sorting_check(sorting_algorithm: ArraySorting) -> None:
    array = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 200
    decorator = ExecutionTimeDecorator(sorting_algorithm)
    decorator.sort(array)
    print(f'Sorted array: {array}')


def main():
    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 200
    print(f'Initial array: {arr}')

    print('\n\n~~~~ Quick Sort ~~~~')
    quick_sort = QuickSort()
    sorting_check(quick_sort)

    print('\n\n~~~~ Multithreading Quick Sort ~~~~')
    multithreading_quick_sort = MultithreadingQuickSort()
    sorting_check(multithreading_quick_sort)

    print('\n\n~~~~ Merge Sort ~~~~')
    merge_sort = MergeSort()
    sorting_check(merge_sort)

    print('\n\n~~~~ Multithreading Merge Sort ~~~~')
    multithreading_merge_sort = MultithreadingMergeSort()
    sorting_check(multithreading_merge_sort)


if __name__ == '__main__':
    main()
