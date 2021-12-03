from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

total_lines = 0
counters = [0] * 12

with open(BASE_DIR / '../input.txt') as f:
    for line in f:
        total_lines += 1
        counters = [int(a) + b for a, b in zip(line.rstrip('\n'), counters)]

    half_lines = total_lines / 2
    binaries_gamma_rate = [str(1) if i > half_lines else str(0) for i in counters]
    binaries_epsilon_rate = [str(0) if i > half_lines else str(1) for i in counters]
    gamma_rate = int(''.join(binaries_gamma_rate), 2)
    epsilon_rate = int(''.join(binaries_epsilon_rate), 2)
    print(f'Result: {gamma_rate * epsilon_rate}')
