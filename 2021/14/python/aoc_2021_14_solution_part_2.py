from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent
MAX_STEPS = 10
cache = {}


def merge_counters(counters_this_step, counter_step_over):
    for letter in counter_step_over:
        if letter not in counters_this_step:
            counters_this_step[letter] = counter_step_over.get(letter)
        else:
            counters_this_step[letter] = counters_this_step.get(letter) + counter_step_over.get(letter)


def update_counters(pair_insertion_rules, rule, step, max_steps=MAX_STEPS):
    if step > max_steps:
        return {}

    if (step, rule) in cache:
        return cache.get((step, rule))
    else:
        counters = {}
        letter = pair_insertion_rules.get(rule)
        counters[letter] = 1

        merge_counters(counters, update_counters(pair_insertion_rules, rule[0] + letter, step + 1, max_steps))
        merge_counters(counters, update_counters(pair_insertion_rules, letter + rule[1], step + 1, max_steps))
        cache[(step, rule)] = counters
        return counters


def count_polymer(template, counters):
    letters = set(template)
    for letter in letters:
        counters[letter] = template.count(letter)


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

        polymer_template = rows[0]
        # polymer_template = 'CK'
        print(polymer_template)

        pair_insertion_rules = {}
        for row in rows[2:]:
            split_row = row.split(' -> ')
            pair_insertion_rules[split_row[0]] = split_row[1]

        counters = {}
        count_polymer(polymer_template, counters)

        for i in range(len(polymer_template) - 1):
            merge_counters(counters, update_counters(pair_insertion_rules, polymer_template[i:i + 2], 1, 40))

        counters_sorted = {k: v for k, v in sorted(counters.items(), key=lambda item: item[1])}

        min_count = counters_sorted.get(list(counters_sorted)[0])
        max_count = counters_sorted.get(list(counters_sorted)[-1])

        print(f'Result: {max_count - min_count}')


if __name__ == '__main__':
    main()
