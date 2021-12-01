
total = 0
total_ribbon = 0

with open('input.txt') as f:
    for line in f:
        sides = [int(x) for x in line.rstrip('\n').split('x')]
        areas = [
            sides[0] * sides[1],
            sides[1] * sides[2],
            sides[2] * sides[0]
        ]

        min_area = min(areas)
        sum_areas = sum([2*i for i in areas])

        total += sum_areas + min_area

        perimeters = [
            sides[0] + sides[1],
            sides[1] + sides[2],
            sides[2] + sides[0]
        ]

        min_perimeter = min(perimeters)
        total_ribbon += min_perimeter * 2 + sides[0] * sides[1] * sides[2]

print(f'Result paper: {total}')
print(f'Result ribbon: {total_ribbon}')

