from pathlib import Path


def process_input(cleaned_lines):
    input = [line.split(' -> ') for line in cleaned_lines]
    return input


def process_point(matrix, points):
    points_0_str = points[0].split(',')
    points_1_str = points[1].split(',')
    x_0 = int(points_0_str[0])
    y_0 = int(points_0_str[1])

    x_1 = int(points_1_str[0])
    y_1 = int(points_1_str[1])

    if x_0 != x_1 and y_0 != y_1:  # diagonal lines
        if x_0 <= x_1 and y_0 <= y_1:  # descend from left to right
            for i in range(x_1 - x_0 + 1):
                matrix[x_0 + i][y_0 + i] += 1
            return

        if x_0 >= x_1 and y_0 > y_1:  # ascend from right to left
            x_0, x_1 = x_1, x_0
            y_0, y_1 = y_1, y_0
            for i in range(x_1 - x_0 + 1):
                matrix[x_0 + i][y_0 + i] += 1
            return

        if x_0 <= x_1 and y_0 > y_1:  # ascend from left to right
            for i in range(x_1 - x_0 + 1):
                matrix[x_0 + i][y_0 - i] += 1
            return

        if x_0 >= x_1 and y_0 < y_1:  # descend from right to left
            x_0, x_1 = x_1, x_0
            y_0, y_1 = y_1, y_0
            for i in range(x_1 - x_0 + 1):
                matrix[x_0 + i][y_0 - i] += 1
            return

    if x_0 == x_1 and y_0 <= y_1:  # Horizontal lines
        for y in range(y_0, y_1 + 1):
            matrix[x_0][y] += 1
        return


    if x_0 == x_1 and y_0 > y_1:  # Horizontal lines
        for y in range(y_0, y_1 - 1, -1):
            matrix[x_0][y] += 1
        return

    if y_0 == y_1 and x_0 <= x_1:  # Horizontal lines
        for x in range(x_0, x_1 + 1):
            matrix[x][y_0] += 1
        return

    if y_0 == y_1 and x_0 > x_1:  # Horizontal lines
        for x in range(x_0, x_1 - 1, -1):
            matrix[x][y_0] += 1
        return


def detect_overlaps(matrix):
    count = 0
    for line in matrix:
        for element in line:
            if element > 1:
                count += 1

    return count


BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(BASE_DIR / '../input.txt') as f:
    # Load input
    cleaned_lines = f.read().splitlines()
    input = process_input(cleaned_lines)
    matrix = [[0] * 1000 for i in range(1000)]
    for line in input:
        process_point(matrix, line)

    # for line in matrix:
    #     print(line)

    count = detect_overlaps(matrix)

    print(f'Result: {count}')
