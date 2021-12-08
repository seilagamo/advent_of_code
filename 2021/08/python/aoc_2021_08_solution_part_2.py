from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def decode_segments(segments):
    result = {}
    segments.sort(key=len)

    result[segments[0]] = '1'
    result[segments[1]] = '7'
    result[segments[2]] = '4'
    result[segments[9]] = '8'

    reverse_result = inv_map = {v: k for k, v in result.items()}

    # We need to know the 3 number
    for i in segments[3: 6]:
        if set(reverse_result.get('7')).issubset(set(i)):
            result[i] = '3'
            reverse_result['3'] = i
            break

    nine = ''.join(set(reverse_result.get('3')) | set(reverse_result.get('4')))
    result[nine] = '9'
    reverse_result['9'] = nine

    # Search for 6 and 0
    for i in segments[6:9]:
        if not set(reverse_result.get('7')).issubset(set(i)):
            result[i] = '6'
            reverse_result['6'] = i
        elif set(i) != set(reverse_result.get('9')):
            result[i] = '0'
            reverse_result['0'] = i

    # Search for 5 and 2
    for i in segments[3: 6]:
        if set(i) != set(reverse_result.get('3')) and set(i).issubset(reverse_result.get('9')):
            result[i] = '5'
            reverse_result['5'] = i
        elif set(i) != set(reverse_result.get('3')) and not set(i).issubset(reverse_result.get('9')):
            result[i] = '2'
            reverse_result['2'] = i

    return result


with open(BASE_DIR / '../input.txt') as f:
    # Load input
    clean_lines = f.read().splitlines()
    count = 0
    for clean_line in clean_lines:

        first_group_of_digits, second_group_of_digits = clean_line.split(' | ')

        decoded_digits = decode_segments(first_group_of_digits.split(' '))

        line_output = ''
        for group in second_group_of_digits.split(' '):
            for key in decoded_digits.keys():
                if set(group) == set(key):
                    line_output += decoded_digits.get(key)
        print(line_output)
        count += int(line_output)

    print(f'Result: {count}')
