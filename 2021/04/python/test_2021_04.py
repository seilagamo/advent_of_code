from .aoc_2021_04_solution_part_1 import has_row, has_column

def test_has_row_completed():
    data = [
        ['79', '71', '82', '1', '77'],  # From (0, 0) to (0, 4)
        ['96', '39', '24', '60', '81'],  # From (1, 0) to (1, 4)
        ['49', '16', '12', '63', '14'],
        ['0', '32', '78', '37', '8'],
        ['92', '33', '15', '99', '65']  # From (4, 0) to (4, 4)
    ]

    result = has_row(data, ['0', '32', '78', '37', '8'])
    assert result

def test_has_column_completed():
    data = [
        ['79', '71', '82', '1', '77'],  # From (0, 0) to (0, 4)
        ['96', '39', '24', '60', '81'],  # From (1, 0) to (1, 4)
        ['49', '16', '12', '63', '14'],
        ['0', '32', '78', '37', '8'],
        ['92', '33', '15', '99', '65']  # From (4, 0) to (4, 4)
    ]

    result = has_column(data, ['79', '96', '49', '0', '92'])
    assert result

