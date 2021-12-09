from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / '../input.txt') as f:
    # Load input
    clean_line = f.read().splitlines()
    positions = [int(position) for position in clean_line[0].split(',')]

    min_fuel = 0
    optimal_position = 0
    sums = {}
    for i, position in enumerate(positions):
        fuel = 0
        for j, other_position in enumerate(positions):
            if i == j:
                continue
            difference = abs(position - other_position)
            if difference in sums:
                fuel += sums.get(difference)
            else:
                sums[difference] = sum(range(abs(position - other_position) + 1))
                fuel += sums[difference]

        if (min_fuel != 0 and fuel < min_fuel) or min_fuel == 0:
            min_fuel = fuel
            optimal_position = position

    print(f'Result: {min_fuel}')
