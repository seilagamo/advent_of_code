from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def is_incomplete(line):
    open_chunks = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    my_stack = deque()

    for chunk in line:
        if chunk in ('(', '[', '{', '<'):
            my_stack.append(chunk)
        elif chunk in (')', ']', '}', '>'):
            try:
                dequed_chunk = my_stack.pop()
                if dequed_chunk != open_chunks.get(chunk):
                    return chunk, False
            except IndexError:
                return chunk, False

    return (my_stack, True) if my_stack else (None, False)


def calculate_score(my_stack):
    chunk_points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    total = 0
    while my_stack:
        total = total * 5 + chunk_points.get(my_stack.pop())

    return total


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        lines = f.read().splitlines()
        scores = []
        for line in lines:
            remaining_chunks, _is_incomplete = is_incomplete(line)
            if _is_incomplete:
                scores.append(calculate_score(remaining_chunks))

        scores.sort()

        middle = scores[len(scores) // 2]
        print(f'Result: {middle}')


if __name__ == '__main__':
    main()
