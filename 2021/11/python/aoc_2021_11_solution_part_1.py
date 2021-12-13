from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def flash_position(matrix, i, j):
    new_positions = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1)
    ]

    for position in new_positions:
        if 0 <= position[0] < len(matrix) and \
                0 <= position[1] < len(matrix[position[0]]) and \
                matrix[position[0]][position[1]] > 0:
            matrix[position[0]][position[1]] += 1
            if matrix[position[0]][position[1]] > 9:
                matrix[position[0]][position[1]] = 0
                flash_position(matrix, position[0], position[1])


def count_flashes_to_step(matrix, steps):
    count = 0
    print()
    for _ in range(steps):
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                matrix[i][j] += 1

        for i, row in enumerate(matrix):
            print(row)
            for j, column in enumerate(row):
                if matrix[i][j] > 9:  # flash
                    matrix[i][j] = 0
                    flash_position(matrix, i, j)
        print()
        for i, row in enumerate(matrix):
            print(row)
            for j, column in enumerate(row):
                if matrix[i][j] == 0:
                    count += 1

    return count


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

        matrix = []
        for row in rows:
            matrix.append([int(number) for number in row])

        count = count_flashes_to_step(matrix, 100)

        print(f'Result: {count}')


if __name__ == '__main__':
    main()
