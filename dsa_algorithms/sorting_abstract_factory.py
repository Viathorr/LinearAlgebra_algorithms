from .array_sorting import *
from abc import ABC, abstractmethod


# TODO implement singleton pattern for sorting abstract factory


class SortingAbstractFactory(ABC):
    @abstractmethod
    def create_quick_sorting(self):
        pass

    @abstractmethod
    def create_merge_sorting(self):
        pass


class SortingFactory(SortingAbstractFactory):
    def create_quick_sorting(self):
        return ArraySortingProxy(QuickSort())

    def create_merge_sorting(self):
        return ArraySortingProxy(MergeSort())


class MultithreadedSortingFactory(SortingFactory):
    def create_quick_sorting(self):
        return ArraySortingProxy(MultithreadingQuickSort())

    def create_merge_sorting(self):
        return ArraySortingProxy(MultithreadingMergeSort())
