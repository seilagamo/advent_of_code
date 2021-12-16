from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def insert_into_template(template, character, index):
    result = template[:index] + character + template[index:]
    return result


def apply_rules_to_template(template, rules):
    result = template
    count_inserts = 0
    for i in range(len(template)):
        if template[i:i + 2] in rules:
            new_i = i + count_inserts
            result = insert_into_template(result, rules.get(template[i:i + 2]), new_i + 1)
            count_inserts += 1

    return result


def count_result(result):
    counters = {}
    letters = set(result)
    for letter in letters:
        counters[letter] = result.count(letter)

    return counters


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

        polymer_template = rows[0]

        pair_insertion_rules = {}
        for row in rows[2:]:
            split_row = row.split(' -> ')
            pair_insertion_rules[split_row[0]] = split_row[1]

        result = polymer_template
        for _ in range(10):
            result = apply_rules_to_template(result, pair_insertion_rules)

        counters = count_result(result)

        counters_sorted = {k: v for k, v in sorted(counters.items(), key=lambda item: item[1])}

        min_count = counters_sorted.get(list(counters_sorted)[0])
        max_count = counters_sorted.get(list(counters_sorted)[-1])

        print(f'Result: {max_count - min_count}')

if __name__ == '__main__':
    main()
