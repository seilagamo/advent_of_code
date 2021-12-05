from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def process_input(cleaned_lines):
    boards = []
    new_board = []
    for i, line in enumerate(cleaned_lines):
        if i == 0:
            random_numbers = line.split(',')
            continue

        if not line:
            if new_board:
                boards.append(new_board.copy())

            new_board.clear()
            continue
        else:
            elements = [number.strip() for number in line.strip().split(' ')]
            row = [element for element in elements if element]
            new_board.append(row.copy())

    return random_numbers, boards


def has_row(board, numbers):
    for row in board:
        if set(row).issubset(set(numbers)):
            return True
    return False


def has_column(board, numbers):
    for i in range(5):
        column = [row[i] for row in board]
        if set(column).issubset(set(numbers)):
            return True
    return False


def get_unmarked_numbers(board, numbers):
    set_board = set()
    for row in board:
        set_board.update(row)

    return set_board - set(numbers)


with open(BASE_DIR / '../input.txt') as f:
    # Load input
    cleaned_lines = f.read().splitlines()
    random_numbers, boards = process_input(cleaned_lines)

    # for board in boards:
    #     print(board)
    #
    # print(random_numbers)

    processed_numbers = []
    has_winner = False
    last_board = []
    last_processed_numbers = []
    for number in random_numbers:
        processed_numbers.append(number)
        for i, board in enumerate(boards):
            if has_column(board, processed_numbers) or has_row(board, processed_numbers):
                last_board = board.copy()
                last_processed_numbers = processed_numbers.copy()
                boards.remove(board)

    str_elements = get_unmarked_numbers(last_board, last_processed_numbers)
    sum_elements = sum([int(element) for element in str_elements])
    print(f'Result {sum_elements * int(last_processed_numbers[-1])}')

