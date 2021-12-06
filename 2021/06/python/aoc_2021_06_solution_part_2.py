from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent
MAX = 256

counts = {}


def count_children(number, total_loop, max_loop=MAX):
    if max_loop <= total_loop:
        counts[(number, total_loop)] = 0
        return 0

    if number in (7, 8):
        d = max_loop + 1 - total_loop - (number - 6)
    else:
        d = max_loop + 1 - total_loop + (6 - number)

    children = d // 7

    count = children
    for i in range(0, children):
        loop_number = 7 * i + (number + 1 + total_loop)
        if (8, loop_number) in counts:
            count += counts[(8, loop_number)]
        else:
            partial_count = count_children(8, 7 * i + (number + 1 + total_loop), max_loop)
            counts[(8, loop_number)] = partial_count
            count += partial_count

    return count


with open(BASE_DIR / '../input.txt') as f:
    # Load input
    clean_line = f.read().splitlines()
    internal_times = [int(internal_time) for internal_time in clean_line[0].split(',')]
    # print(internal_times)
    count = 0

    count += count_children(0, 1, MAX) * internal_times.count(0)
    count += count_children(1, 1, MAX) * internal_times.count(1)
    count += count_children(2, 1, MAX) * internal_times.count(2)
    count += count_children(3, 1, MAX) * internal_times.count(3)
    count += count_children(4, 1, MAX) * internal_times.count(4)
    count += count_children(5, 1, MAX) * internal_times.count(5)
    count += count_children(6, 1, MAX) * internal_times.count(6)
    count += count_children(7, 1, MAX) * internal_times.count(7)
    count += count_children(8, 1, MAX) * internal_times.count(8)

    count += len(internal_times)

    print(f'Result: {count}')
