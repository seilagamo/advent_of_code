from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def fold_matrix(matrix, fold):
    if fold[1] == 0:  # fold along x -> vertical
        for y, row in enumerate(matrix):
            second_half_row_reversed = row[:fold[0] - 1: -1]
            for x, column in enumerate(row):
                if x >= fold[0]:
                    break
                if second_half_row_reversed[x] == '#':
                    matrix[y][x] = second_half_row_reversed[x]

            del matrix[y][fold[0]:]

    elif fold[0] == 0:  # fold along y -> horizontal
        second_half_matrix_reversed = matrix[:fold[1] - 1: -1]
        for y, row in enumerate(matrix):
            if y >= fold[1]:
                break
            for x, column in enumerate(row):
                if second_half_matrix_reversed[y][x] == '#':
                    matrix[y][x] = second_half_matrix_reversed[y][x]

        del matrix[fold[1]:]


def count_dots(matrix):
    total_dots = 0

    for y, row in enumerate(matrix):
        for x, column in enumerate(row):
            total_dots += 1 if matrix[y][x] == '#' else 0

    return total_dots


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

    coordinates = []
    folds = []
    are_points = True

    max_x = 0
    max_y = 0

    for row in rows:
        if not row:
            are_points = False
            continue

        if are_points:
            split_row = row.split(',')
            coordinates.append((int(split_row[0]), int(split_row[1])))

        if not are_points:
            split_row = row.split()[-1].split('=')
            if split_row[0] == 'x':  # vertical fold
                x = int(split_row[1])
                if x > max_x:
                    max_x = x
                folds.append((x, 0))
            elif split_row[0] == 'y':  # horizontal fold
                y = int(split_row[1])
                if y > max_y:
                    max_y = y
                folds.append((0, y))

    # build the matrix
    matrix = [x[:] for x in [['.'] * (max_x * 2 + 1)] * (max_y * 2 + 1)]

    print(len(matrix))

    # Set values from coordinates
    for coordinate in coordinates:
        matrix[coordinate[1]][coordinate[0]] = '#'

    for fold in folds:
        fold_matrix(matrix, fold)

    print()
    print('Matrix: ')
    for row in matrix:
        # print(''.join(row))
        print(row)


if __name__ == '__main__':
    main()
