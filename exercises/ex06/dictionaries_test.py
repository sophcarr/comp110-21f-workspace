"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730320301"


def test_invert() -> None:
    """Testing invert with basic input."""
    list1: dict[str, str] = {'apple': 'cat'}
    assert invert(list1) == {'cat': 'apple'}


def test_invert_again() -> None:
    """Testing invert with more complicated input."""
    list1: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(list1) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_edge_case() -> None:
    """Testing invert edge case when there is an empty dictionary."""
    list1: dict[str, str] = {}
    assert invert(list1) == {}


def test_favorite_color() -> None:
    """Testing favorite_color with basic input."""
    list1: dict[str, str] = {'Sophia': 'Yellow', 'Vivian': 'Purple', 'Marc': 'Yellow'}
    assert favorite_color(list1) == "Yellow"


def test_favorite_color_again() -> None:
    """Testing favorite_color with more commplicated input."""
    list1: dict[str, str] = {'Sophia': 'Purple', 'Vivian': 'Blue', 'Marc': 'Yellow', 'Sarah': 'Purple', 'Steve': 'Purple'}
    assert favorite_color(list1) == "Purple"


def test_favorite_color_edge() -> None:
    """Testing favorite_color when there is a tie."""
    list1: dict[str, str] = {'Sophia': 'Purple', 'Vivian': 'Blue', 'Marc': 'Purple', 'Sarah': 'Blue', 'Steve': 'Green'}
    assert favorite_color(list1) == "Purple"


def test_count() -> None:
    """Testing count with basic input."""
    list1: list[str] = ['a', 'b', 'c']
    assert count(list1) == {'a': 1, 'b': 1, 'c': 1}


def test_count_again() -> None:
    """Testing count with more complicated input."""
    list1: list[str] = ['a', 'b', 'c', 'a', 'a']
    assert count(list1) == {'a': 3, 'b': 1, 'c': 1}


def test_count_edge() -> None:
    """Testing count when given an empty list."""
    list1: list[str] = []
    assert count(list1) == {}