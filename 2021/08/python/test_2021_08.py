from .aoc_2021_08_solution_part_2 import decode_segments


def test_decode_segments():
    input = 'fgabec gefb cdagefb fbacgd dgecba adecf eg cefga egc gcfba'

    decoded_numbers = decode_segments(input.split(' '))

    print()
    print(decoded_numbers)

    assert len(decoded_numbers) == 10

