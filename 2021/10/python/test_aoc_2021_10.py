import pytest

from .aoc_2021_10_solution_part_1 import is_valid_line
from .aoc_2021_10_solution_part_2 import is_incomplete, calculate_score


@pytest.mark.parametrize(
    'test_input',
    [
        '()',
        '([])',
        '{()()()}',
        '<([{}])>',
        '[<>({}){}[([])<>]]',
        '(((((((((())))))))))',
        '[({(<(())[]>[[{[]{<()<>>'

    ]
)
def test_ok(test_input):
    chunk, is_valid = is_valid_line(test_input)
    assert is_valid


@pytest.mark.parametrize(
    'test_input',
    [
        '(]',
        '{()()()>',
        '(((()))}',
        '<([]){()}[{}])'
        '{([(<{}[<>[]}>{[]{[(<()>',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
    ]
)
def test_ko(test_input):
    chunk, is_valid = is_valid_line(test_input)
    assert not is_valid
    assert chunk in (')', ']', '}', '>')


@pytest.mark.parametrize(
    'test_input',
    [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '(((({<>}<{<{<>}{[]{[]{}',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ]
)
def test_incomplete(test_input):
    _, is_valid = is_valid_line(test_input)
    assert is_valid


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('[({(<(())[]>[[{[]{<()<>>', 288957),
        ('[(()[<>])]({[<{<<[]>>(', 5566),
        ('(((({<>}<{<{<>}{[]{[]{}', 1480781),
        ('{<[[]]>}<{[{[{[]{()[[[]', 995444),
        ('<{([{{}}[<[[[<>{}]]]>[]]', 294)


    ]
)
def test_calculate_score(test_input, expected):
    my_stack, _is_incomplete = is_incomplete(test_input)

    assert _is_incomplete

    score = calculate_score(my_stack)
    assert score == expected
