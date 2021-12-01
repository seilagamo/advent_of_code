def calculate_product(lines):
    for line_a in lines:
        for line_b in lines:
            if line_a + line_b == 2020:
                return line_a * line_b


def calculate_sum(lines):
    for line_a in lines:
        for line_b in lines:
            for line_c in lines:
                if line_a + line_b + line_c == 2020:
                    return line_a, line_b, line_c


lines = []
with open('input.txt') as f:
    for cnt, line in enumerate(f):
        lines.append(int(line))


print(calculate_product(lines))

a, b, c = calculate_sum(lines)
print(f'The three numbers that sums 2020 are {a}, {b}, {c}')
print(f'The product are: {a * b * c}')
