from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / '../input.txt') as f:
    # Load input
    clean_lines = f.read().splitlines()
    count = 0
    for clean_line in clean_lines:
        second_group_of_digits = clean_line.split(' | ')[1].split(' ')
        line = [len(segment) for segment in second_group_of_digits if len(segment) in (2, 4, 3, 7)]
        count += len(line)

    print(f'Result: {count}')
