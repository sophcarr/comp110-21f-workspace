"""Utility functions."""

__author__ = "730320301"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Making a column-based table with only the first N rows of data for each  column."""
    result: dict[str, list[str]] = {}
    i: int = 0

    for column in table:
        row: list[str] = []
        if len(table) >= N:
            while i < N:
                row.append(table[column][i])
                i += 1
            result[column] = row
            i = 0
        else:
            result = table
    return result


def select(table: dict[str, list[str]], hello: list[str]) -> dict[str, list[str]]:
    """Selecting specific columns."""
    result: dict[str, list[str]] = {}

    for column in hello: 
        result[column] = table[column]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two dictionarires."""
    result: dict[str, list[str]] = {}

    for column in a:
        result[column] = a[column]
    for column in b:
        if column in result:
            result[column] += b[column]
        else:
            result[column] = b[column]
    return result


def count(hi: list[str]) -> dict[str, int]:
    """Number of times a value appeared in input list."""
    result: dict[str, int] = {}
    i: int = 0

    while i < len(hi):
        if hi[i] in result:
            result[hi[i]] += 1
        else:
            result[hi[i]] = 1
        i += 1
    return result
