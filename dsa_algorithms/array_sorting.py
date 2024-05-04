from abc import ABC, abstractmethod
import time
from threading import Thread


class ArraySorting(ABC):
    @abstractmethod
    # Array is passed by ref, so it is changed automatically
    def sort(self, array: list[int | float]) -> None:
        pass


class ExecutionTimeDecorator(ArraySorting):
    def __init__(self, alg: ArraySorting):
        self.__algorithm = alg

    def sort(self, array: list[int | float]) -> None:
        start = time.time()
        self.__algorithm.sort(array)
        print(f'Sorting execution time: {time.time() - start:.6f}s')


class AQuickSort(ArraySorting):
    def sort(self, array: list[int | float]) -> None:
        self._quick_sort(array, 0, len(array) - 1)

    @abstractmethod
    def _quick_sort(self, array: list[int | float], beg: int, end: int) -> None:
        pass

    def _partition(self, array: list[int | float], beg: int, end: int) -> int:
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
    def _quick_sort(self, array: list[int | float], beg: int, end: int) -> None:
        if beg <= end:
            pivot_index = self._partition(array, beg, end)
            self._quick_sort(array, beg, pivot_index - 1)
            self._quick_sort(array, pivot_index + 1, end)


class MultithreadingQuickSort(AQuickSort):
    def __init__(self):
        self._quick_sorting = QuickSort()

    def _quick_sort(self, array: list[int | float], beg: int, end: int) -> None:
        if beg <= end:
            pivot_index = self._partition(array, beg, end)

            th_1 = Thread(target=self._quick_sort, args=(array, beg, pivot_index - 1))
            th_2 = Thread(target=self._quick_sort, args=(array, pivot_index + 1, end))

            th_1.start()
            th_2.start()

            th_1.join()
            th_2.join()


class AMergeSort(ArraySorting):
    def sort(self, array: list[int | float]) -> None:
        self._merge_sort(array)

    @abstractmethod
    def _merge_sort(self, array: list[int | float]):
        pass

    def _merge(self, array: list[int | float], left: list[int | float], right: list[int | float]):
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
    def _merge_sort(self, array: list[int | float]):
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]
        self._merge_sort(left)
        self._merge_sort(right)
        self._merge(array, left, right)


class MultithreadingMergeSort(AMergeSort):
    def _merge_sort(self, array: list[int | float]):
        if len(array) < 2:
            return
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        th_1 = Thread(target=self._merge_sort, args=(left,))
        th_2 = Thread(target=self._merge_sort, args=(right,))

        th_1.start()
        th_2.start()

        th_1.join()
        th_2.join()

        self._merge(array, left, right)


def main():
    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 150

    print('~~~~ Quick Sort ~~~~')
    print(f'Initial array: {arr}')
    quick_sort = QuickSort()
    decorator = ExecutionTimeDecorator(quick_sort)
    decorator.sort(arr)
    print(f'Sorted array: {arr}')

    print('~~~~ Multithreading Quick Sort ~~~~')
    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 150
    print(f'Initial array: {arr}')
    multithreading_quick_sort = MultithreadingQuickSort()
    decorator = ExecutionTimeDecorator(multithreading_quick_sort)
    decorator.sort(arr)
    print(f'Sorted array: {arr}')

    print('\n\n~~~~ Merge Sort ~~~~')
    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 150
    print(f'Initial array: {arr}')
    merge_sort = MergeSort()
    decorator = ExecutionTimeDecorator(merge_sort)
    decorator.sort(arr)
    print(f'Sorted array: {arr}')

    print('\n\n~~~~ Multithreading Merge Sort ~~~~')
    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 150
    print(f'Initial array: {arr}')
    multithreading_merge_sort = MultithreadingMergeSort()
    decorator = ExecutionTimeDecorator(multithreading_merge_sort)
    decorator.sort(arr)
    print(f'Sorted array: {arr}')


if __name__ == '__main__':
    main()
