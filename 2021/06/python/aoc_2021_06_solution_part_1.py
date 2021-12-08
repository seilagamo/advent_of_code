from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / '../input.txt') as f:
    # Load input
    clean_line = f.read().splitlines()
    internal_times = [int(internal_time) for internal_time in clean_line[0].split(',')]
    # print(internal_times)

    count_0 = internal_times.count(0)

    for i in range(1, 80+1):
        internal_times = [internal_time - 1 if internal_time > 0 else 6 for internal_time in internal_times]
        internal_times.extend([8] * count_0)
        count_0 = internal_times.count(0)

    print(f'Result: {len(internal_times)}')
