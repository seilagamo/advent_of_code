from .aoc_2021_13_solution_part_2 import fold_matrix, count_dots


def test_fold_horizontal():
    input = [
        '...#..#..#.',
        '....#......',
        '...........',
        '#..........',
        '...#....#.#',
        '...........',
        '...........',
        '...........',
        '...........',
        '...........',
        '.#....#.##.',
        '....#......',
        '......#...#',
        '#..........',
        '#.#........'
    ]
    matrix = []
    for row in input:
        matrix.append([c for c in row])

    fold_matrix(matrix, (0, 7))
    count = count_dots(matrix)
    assert count == 17


def test_fold_vertical():
    input = [
        '#.##..#..#.',
        '#...#......',
        '......#...#',
        '#...#......',
        '.#.#..#.###',
        '...........',
        '...........'
    ]

    matrix = []
    for row in input:
        matrix.append([c for c in row])

    print()
    for row in matrix:
        print(row)

    fold_matrix(matrix, (5, 0))
    print()
    for row in matrix:
        print(row)
    count = count_dots(matrix)
    assert count == 16
