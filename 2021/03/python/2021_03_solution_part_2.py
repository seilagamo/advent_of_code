from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / '../input.txt') as f:
    cleaned_lines = f.read().splitlines()

    filtered = cleaned_lines.copy()
    for i in range(12):
        total_lines = 0
        counter_0 = 0
        counter_1 = 0
        previous_filtered = filtered.copy()
        for line in filtered:
            counter_0 += 1 if line[i] == '0' else 0
            counter_1 += 1 if line[i] == '1' else 0

        most_common = 1 if counter_1 >= counter_0 else 0
        filtered = [line for line in filtered if line[i] == str(most_common)]
        if not filtered:
            filtered = [previous_filtered[-1]]
            break

    oxygen_generator_rating = int(filtered[0], 2)

    filtered = cleaned_lines.copy()
    for i in range(12):
        counter_0 = 0
        counter_1 = 0
        previous_filtered = filtered.copy()
        for line in filtered:
            counter_0 += 1 if line[i] == '0' else 0
            counter_1 += 1 if line[i] == '1' else 0

        less_common = 1 if counter_1 < counter_0 else 0
        filtered = [line for line in filtered if line[i] == str(less_common)]
        if not filtered:
            filtered = [previous_filtered[-1]]
            break

    co2_scrubber_rating = int(filtered[0], 2)

    print(f'Result: {oxygen_generator_rating * co2_scrubber_rating}')



