import pytest
from ..array_sorting import MultithreadingMergeSort
from ..array_sorting_proxy import ArraySortingProxy


@pytest.fixture
def multithreaded_merge_sort():
    multithreaded_merge_sort = MultithreadingMergeSort()
    return ArraySortingProxy(multithreaded_merge_sort)


def test_raises_type_error(multithreaded_merge_sort, invalid_array):
    with pytest.raises(TypeError):
        multithreaded_merge_sort.sort(invalid_array)


def test_sort_empty_array(multithreaded_merge_sort, empty_array):
    multithreaded_merge_sort.sort(empty_array)
    assert empty_array == []


def test_sort_one_element_array(multithreaded_merge_sort, one_element_array):
    multithreaded_merge_sort.sort(one_element_array)
    assert one_element_array == [1]


def test_sort_same_num_array(multithreaded_merge_sort, same_num_array):
    multithreaded_merge_sort.sort(same_num_array)
    assert same_num_array == [2, 2, 2, 2, 2, 2]


def test_sort_positive_array(multithreaded_merge_sort, positive_array):
    multithreaded_merge_sort.sort(positive_array)
    assert positive_array == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sort_negative_array(multithreaded_merge_sort, negative_array):
    multithreaded_merge_sort.sort(negative_array)
    assert negative_array == [-9, -8, -7, -6, -5, -4, -3, -2, -1]


def test_sort_mixed_array(multithreaded_merge_sort, mixed_array):
    multithreaded_merge_sort.sort(mixed_array)
    assert mixed_array == [-34, -4, -1, 2, 3, 4, 9, 11]


def test_float_array(multithreaded_merge_sort, float_nums_array):
    multithreaded_merge_sort.sort(float_nums_array)
    assert float_nums_array == [-3.0, -2.7, -1.1, 0.5, 3.14, 5.6, 8.9]


def test_sort_string_array(multithreaded_merge_sort, string_array):
    multithreaded_merge_sort.sort(string_array)
    assert string_array == ['a', 'b', 'bewo', 'cwa', 'vda']