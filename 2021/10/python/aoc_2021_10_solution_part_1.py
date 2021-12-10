from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def is_valid_line(line):
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
    return None, True


def main():
    chunk_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        lines = f.read().splitlines()
        total = 0
        for line in lines:
            chunk, is_valid = is_valid_line(line)
            if not is_valid:
                total += chunk_points.get(chunk)

        print(f'Result: {total}')


if __name__ == '__main__':
    main()
