with open('input.txt') as f:
    count = 0
    A = 0
    B = 0
    C = 0
    current = 0
    previous = 0
    for line in f:
        previous = current
        B, C = A, B
        A = int(line.rstrip('\n'))
        if A and B and C:
            current = A + B + C
        if previous and current > previous:
            count += 1

    print(f'Total: {count}')
