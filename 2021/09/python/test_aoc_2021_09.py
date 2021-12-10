from .aoc_2021_09_solution_part_2 import positions_basin


def test_basin():
    rows = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]
    matrix = []
    for row in rows:
        matrix.append([int(number) for number in row])
    positions = {(0, 1)}
    size = 1 + positions_basin(0, 1, matrix, positions)
    assert size == 3


def test_basin_2():
    rows = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]
    matrix = []
    for row in rows:
        matrix.append([int(number) for number in row])
    positions = {(0, 9)}
    size = 1 + positions_basin(0, 9, matrix, positions)
    assert size == 9


def test_basin_3():
    rows = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]

    matrix = []
    for row in rows:
        matrix.append([int(number) for number in row])
    positions = {(2, 2)}
    size = 1 + positions_basin(2, 2, matrix, positions)
    assert size == 14


def test_basin_4():
    rows = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]

    matrix = []
    for row in rows:
        matrix.append([int(number) for number in row])
    positions = {(4, 6)}
    size = 1 + positions_basin(4, 6, matrix, positions)
    assert size == 9
