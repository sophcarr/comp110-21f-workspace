"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


__author__ = "730320301"


def test_only_evens() -> None:
    """Testing only_evens."""
    xs: list[int] = [3, 6]
    assert only_evens(xs) == [6]


def test_only_evens_with_negative_numbers() -> None:
    """Testing only_evens with negative numbers."""
    xs: list[int] = [-5, -4, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [-4, 2, 4, 6]


def test_only_evens_edge_case() -> None:
    """Testing only_evens edge case at one."""
    xs: list[int] = [-4, 1, 2, 3, 6]
    assert only_evens(xs) == [-4, 2, 6]


def test_sub() -> None:
    """Testing sub."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6]
    y: int = 3
    z: int = 1
    assert sub(a_list, y, z) == [2, 3, 4, 5]


def test_sub_when_neg() -> None:
    """Testing sub when starting number is negative."""
    a_list: list[int] = [-3, 4, 5]
    y: int = -3
    z: int = 1
    assert sub(a_list, y, z) == [-3, 4]


def test_sub_edge_case() -> None:
    """Testing edge case for sub when y = 0."""
    a_list: list[int] = [10, 20, 30, 40]
    y: int = 0
    z: int = 3
    assert sub(a_list, y, z) == []


def test_concat() -> None:
    """Testing concat."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    y: list[int] = [555, 33, 1353]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6, 555, 33, 1353]


def test_concat_again() -> None:
    """Testing concat part two."""
    x: list[int] = [1, 1, 1111]
    y: list[int] = [2, 2, 2222]
    assert concat(x, y) == [1, 1, 1111, 2, 2, 2222]


def test_concat_edge_case() -> None:
    """Testing concat for edge case."""
    x: list[int] = [1, 1, 1111]
    y: list[int] = []
    assert concat(x, y) == [1, 1, 1111]