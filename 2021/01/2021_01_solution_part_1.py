with open('input.txt') as f:
    count = 0
    current = 0
    previous = 0
    for line in f:
        previous = current
        current = int(line.rstrip('\n'))
        if previous and current > previous:
            count += 1

    print(f'Total: {count}')
