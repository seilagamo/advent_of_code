from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

indications = {
    'up': (0, -1, 0),
    'forward': (1, 0, 1),
    'down': (0, 1, 0)
}

location = [0, 0, 0]
with open(BASE_DIR / '../input.txt') as f:
    for line in f:
        instruction = line.rstrip('\n').split(' ')
        location[0] += indications[instruction[0]][0] * int(instruction[1])
        location[1] += indications[instruction[0]][2] * int(instruction[1]) * location[2]
        location[2] += indications[instruction[0]][1] * int(instruction[1])

    print(f'Result: {location[0] * location[1]}')
