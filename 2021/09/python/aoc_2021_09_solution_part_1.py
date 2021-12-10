from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / '../input.txt') as f:
    # Load input
    rows = f.read().splitlines()

    matrix = []
    for row in rows:
        matrix.append([int(number) for number in row])

    risk = 0
    for i, row in enumerate(matrix):
        print(row)
        for j, column in enumerate(row):
            is_low = True if (j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j] or j - 1 < 0) and \
                             (i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j] or i - 1 < 0) and \
                             (j + 1 < len(row) and matrix[i][j + 1] > matrix[i][j] or j + 1 >= len(row)) and \
                             (i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j] or i + 1 >= len(matrix)) \
                else False

            if is_low:
                risk += matrix[i][j] + 1

    print(f'Result: {risk}')
