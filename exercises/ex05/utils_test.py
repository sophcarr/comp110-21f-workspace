"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


__author__ = "730320301"


def test_sub_edge() -> None:
    """Testing edge case for sub when y = 0."""
    a_list: list[float] = [1, 2, 3, 4, 5, 6]
    x: int = 3
    y: int = 0
    assert final == []


def test_sub() -> None:
    """Testing sub."""
    a_list: list[float] = [1, 2, 3, 4, 5, 6]
    x: int = 3
    y: int = 1
    assert list(final) == [2, 4, 6]


def test_concat() -> None:
    """Testing concat."""
    x: list[float] = [1, 2, 3, 4, 5, 6]
    y: list[float] = [555, 33, 1353]
    assert list(final) == [2, 4, 6]
