from .aoc_2021_14_solution_part_1 import apply_rules_to_template


def test_simpler_example():
    polymer_template = 'NNCB'
    rules = [
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C'
    ]

    pair_insertion_rules = {}
    for row in rules:
        split_row = row.split(' -> ')
        pair_insertion_rules[split_row[0]] = split_row[1]

    result = apply_rules_to_template(polymer_template, pair_insertion_rules)

    assert result == 'NCNBCHB'

    result = apply_rules_to_template(result, pair_insertion_rules)

    assert result == 'NBCCNBBBCBHCB'

    result = apply_rules_to_template(result, pair_insertion_rules)

    assert result == 'NBBBCNCCNBBNBNBBCHBHHBCHB'

    result = apply_rules_to_template(result, pair_insertion_rules)

    assert result == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'