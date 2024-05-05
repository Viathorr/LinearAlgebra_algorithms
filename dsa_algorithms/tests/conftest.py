import pytest


@pytest.fixture
def invalid_array():
    return ['adf', 2, -3.45, [3, 42, 1]]


@pytest.fixture
def empty_array():
    return []


@pytest.fixture
def one_element_array():
    return [1]


@pytest.fixture
def same_num_array():
    return [2, 2, 2, 2, 2, 2]


@pytest.fixture
def positive_array():
    return [5, 2, 8, 7, 1, 3, 9, 4, 6]


@pytest.fixture
def negative_array():
    return [-5, -2, -8, -7, -1, -3, -9, -4, -6]


@pytest.fixture
def mixed_array():
    return [3, -1, 4, 2, -4, 11, -34, 9]


@pytest.fixture
def float_nums_array():
    return [3.14, -1.1, 0.5, -2.7, 5.6, -3.0, 8.9]


@pytest.fixture
def string_array():
    return ['a', 'vda', 'bewo', 'b', 'cwa']
