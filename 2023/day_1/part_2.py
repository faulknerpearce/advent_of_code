def read_file(file):
    with open(file) as text:
        text_lines = text.read().splitlines()
    return text_lines

def find_first_number(line):
    for index in range(len(line)):
        if ord(line[index]) >= 48 and ord(line[index]) <= 57:
            return line[index]
    return None 

def find_last_number(line):
    for index in range(1, len(line)+1):
        if ord(line[-index]) >= 48 and ord(line[-index]) <= 57:
            return line[-index]
    return None 

def find_index(str_line, greater):
    numbers_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,  'nine': 9}
    index = None
    for key in numbers_map.keys():
        try:
            found_index = str_line.index(key)
            if greater == True: 
                if index == None or found_index > index: 
                    index = found_index
                    word = key
                    number = numbers_map[key]
            else: 
                if index == None or found_index < index: 
                    index = found_index
                    word = key
                    number = numbers_map[key]

        except ValueError:
            continue
    if index == None:
        return str_line
    else:
        forward_format = str_line.replace(str(word), str(number))
        return forward_format

def part_two(lines):
    total = 0 
    for line in lines:
        format_str_one = find_index(line, False)
        format_str_two = find_index(format_str_one, True)
        number = find_first_number(format_str_two)
        number += find_last_number(format_str_two)
        # testing 
        print(f'original: {line}, formatted: {format_str_two}, number: {number}')
        total += int(number)
    return total 

my_text = read_file('text.txt')

answer_part_two = part_two(my_text)

print(f'The answer to part two is: {answer_part_two}')