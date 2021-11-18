parens = {'(': 1, ')': -1}


result = 0

with open('input.txt') as f:
    position = 0
    in_basement = False
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            position += 1
            result += parens[c]
            if result == -1 and not in_basement:
                in_basement = True
                print(f'The position of the character that causes Santa to first enter the basement is {position}')


print(f'Santa takes floor {result}')
