from .aoc_2021_06_solution_part_2 import count_elements

def test_count_elements():
    result = count_elements(0, 1, 17)
    assert result > 0
    print()
    print(result)
