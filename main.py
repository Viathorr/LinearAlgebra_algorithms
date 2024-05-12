from dsa_algorithms.sorting_abstract_factory import SortingFactory, MultithreadingSortingFactory
from dsa_algorithms.execution_time_decorator import *


def sorting_check(sorting_algorithm: ArraySorting) -> None:
    """
    Utility function that performs a sorting operation on a random array using a specified sorting algorithm.

    :param sorting_algorithm: A particular sorting algorithm.
    :type sorting_algorithm: ArraySorting
    :return: None
    """
    array = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 50
    print(f'Initial array: {array}')
    decorator = ExecutionTimeDecorator(sorting_algorithm)
    decorator.sort(array)
    print(f'Sorted array: {array}')


def main() -> None:
    """
    Main function to be executed.
    Performs sorting by quick sort and merge sort algorithms, both sequential and multithreading versions.

    :return: None
    """
    sorting_factory = SortingFactory()
    multithread_sorting_factory = MultithreadingSortingFactory()

    print('\n\n~~~~ Quick Sort ~~~~')
    quick_sort = sorting_factory.create_quick_sorting()
    sorting_check(quick_sort)

    print('\n\n~~~~ Multithreading Quick Sort ~~~~')
    multithreading_quick_sort = multithread_sorting_factory.create_quick_sorting()
    sorting_check(multithreading_quick_sort)

    print('\n\n~~~~ Merge Sort ~~~~')
    merge_sort = sorting_factory.create_merge_sorting()
    sorting_check(merge_sort)

    print('\n\n~~~~ Multithreading Merge Sort ~~~~')
    multithreading_merge_sort = multithread_sorting_factory.create_merge_sorting()
    sorting_check(multithreading_merge_sort)


if __name__ == '__main__':
    main()
