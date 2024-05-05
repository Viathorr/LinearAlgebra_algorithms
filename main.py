from dsa_algorithms.sorting_abstract_factory import SortingFactory, MultithreadedSortingFactory
from dsa_algorithms.execution_time_decorator import ExecutionTimeDecorator


def sorting_check(sorting_algorithm) -> None:
    array = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 200
    decorator = ExecutionTimeDecorator(sorting_algorithm)
    decorator.sort(array)
    print(f'Sorted array: {array}')


def main():
    sorting_factory = SortingFactory()
    multithreaded_sorting_factory = MultithreadedSortingFactory()

    arr = [1, 4, 2, 8, 2, 4, 9, 23, 1, 0, -4, -1] * 200
    print(f'Initial array: {arr}')

    print('\n\n~~~~ Quick Sort ~~~~')
    quick_sort = sorting_factory.create_quick_sorting()
    sorting_check(quick_sort)

    print('\n\n~~~~ Multithreading Quick Sort ~~~~')
    multithreading_quick_sort = multithreaded_sorting_factory.create_quick_sorting()
    sorting_check(multithreading_quick_sort)

    print('\n\n~~~~ Merge Sort ~~~~')
    merge_sort = sorting_factory.create_merge_sorting()
    sorting_check(merge_sort)

    print('\n\n~~~~ Multithreading Merge Sort ~~~~')
    multithreading_merge_sort = multithreaded_sorting_factory.create_merge_sorting()
    sorting_check(multithreading_merge_sort)


if __name__ == '__main__':
    main()
