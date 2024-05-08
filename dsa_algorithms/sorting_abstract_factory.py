from .array_sorting_proxy import ArraySortingProxy, QuickSort, MergeSort, MultithreadingQuickSort,\
    MultithreadingMergeSort


class Singleton(type):
    """
    A metaclass implementing the Singleton design pattern.
    The Singleton metaclass ensures that only one instance of a class is created and
    provides a way to access that instance globally.
    This metaclass should be used as a metaclass for classes that should have only
    one instance throughout the lifetime of the program.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Create a new instance of the class if it does not exist, or return the existing instance.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SortingAbstractFactory(metaclass=Singleton):
    """
    Abstract factory for creating instances of sorting algorithm classes.
    This abstract factory is implemented as a singleton to ensure that only one instance
    of each type of Sorting Abstract Factory is created.
    """
    def __new__(cls, *args, **kwargs):
        """
        Prevents direct instantiation of the SortingAbstractFactory abstract class.

        :raises TypeError: If an attempt is made to directly instantiate the SortingAbstractFactory class.
        """
        if cls is SortingAbstractFactory:
            raise TypeError(f'Class {cls.__name__} can\'t be instantiated.')
        return object.__new__(cls)

    def create_quick_sorting(self) -> ArraySortingProxy:
        """
        Abstract method to create an instance of the ArraySorting derived class that performs quick sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs quick sort algorithm.
        """
        pass

    def create_merge_sorting(self) -> ArraySortingProxy:
        """
        Abstract method to create an instance of the ArraySorting derived class that performs merge sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs merge sort algorithm.
        """
        pass


class SortingFactory(SortingAbstractFactory):
    def create_quick_sorting(self) -> ArraySortingProxy:
        """
        Creates an instance of the ArraySorting derived class that performs sequential version of quick sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs quick sort algorithm.
        """
        return ArraySortingProxy(QuickSort())

    def create_merge_sorting(self) -> ArraySortingProxy:
        """
        Creates an instance of the ArraySorting derived class that performs sequential version of merge sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs merge sort algorithm.
        """
        return ArraySortingProxy(MergeSort())


class MultithreadingSortingFactory(SortingFactory):
    def create_quick_sorting(self) -> ArraySortingProxy:
        """
        Creates an instance of the ArraySorting derived class that performs multithreading version of
        quick sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs multithreading version of
         quick sort algorithm.
        """
        return ArraySortingProxy(MultithreadingQuickSort())

    def create_merge_sorting(self) -> ArraySortingProxy:
        """
        Creates an instance of the ArraySorting derived class that performs multithreading version of
        merge sort algorithm.

        :return: An instance of the ArraysSortingProxy derived class that performs multithreading version of
        merge sort algorithm.
        """
        return ArraySortingProxy(MultithreadingMergeSort())
