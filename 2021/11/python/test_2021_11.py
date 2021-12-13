from .aoc_2021_11_solution_part_1 import count_flashes_to_step


def test_step_1():
    input = [
        '11111',
        '19991',
        '19191',
        '19991',
        '11111'
    ]

    matrix = []
    for row in input:
        matrix.append([int(number) for number in row])

    count = count_flashes_to_step(matrix, 1)
    assert count == 9


def test_step_2():

    input = [
        '11111',
        '19991',
        '19191',
        '19991',
        '11111'
    ]

    matrix = []
    for row in input:
        matrix.append([int(number) for number in row])

    count = count_flashes_to_step(matrix, 2)
    assert count == 9
