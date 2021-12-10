from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def positions_basin(i, j, matrix, positions: set):
    size = 0
    if i - 1 >= 0 and matrix[i - 1][j] < 9:
        if (i - 1, j) not in positions:
            positions.add((i - 1, j))
            size += 1 + positions_basin(i - 1, j, matrix, positions)

    if i + 1 < len(matrix) and matrix[i + 1][j] < 9:
        if (i + 1, j) not in positions:
            positions.add((i + 1, j))
            size += 1 + positions_basin(i + 1, j, matrix, positions)

    if j - 1 >= 0 and matrix[i][j - 1] < 9:
        if (i, j - 1) not in positions:
            positions.add((i, j - 1))
            size += 1 + positions_basin(i, j - 1, matrix, positions)

    if j + 1 < len(matrix[i]) and matrix[i][j + 1] < 9:
        if (i, j + 1) not in positions:
            positions.add((i, j + 1))
            size += 1 + positions_basin(i, j + 1, matrix, positions)

    return size


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

        matrix = []
        for row in rows:
            matrix.append([int(number) for number in row])

        sizes = []

        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                is_low = True if (j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j] or j - 1 < 0) and \
                                 (i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j] or i - 1 < 0) and \
                                 (j + 1 < len(row) and matrix[i][j + 1] > matrix[i][j] or j + 1 >= len(row)) and \
                                 (i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j] or i + 1 >= len(matrix)) \
                    else False
                positions = set()
                if is_low:
                    positions.add((i, j))
                    size = 1 + positions_basin(i, j, matrix, positions)
                    sizes.append(size)

        sizes.sort(reverse=True)
        result = sizes[0] * sizes[1] * sizes[2]

        print(f'Result: {result}')


if __name__ == '__main__':
    main()
