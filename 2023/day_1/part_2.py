# Read the contents of a file, split lines, and return as a list
def read_file_return_list(file):
    with open(file) as text:
        text_lines = text.read().splitlines()
    return text_lines

# Find and return the first numeric character in a string.
def find_first_number(line):
    for index in range(len(line)):
        if ord(line[index]) >= 48 and ord(line[index]) <= 57:
            return line[index]
    return None 

# Find and return the last numeric character in a string.
def find_last_number(line):
    for index in range(1, len(line)+1):
        if ord(line[-index]) >= 48 and ord(line[-index]) <= 57:
            return line[-index]
    return None 

# Count the occurrences of numeric words in a string.
def count_occurrences(str_line):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_found = 0
    for word in numbers:
        numbers_found += str_line.count(word) 
    return numbers_found

# Replace numeric words with digits in a string.
def replace_words_for_digits(str_line):
    numbers_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,  'nine': 9}
    numbers_found = count_occurrences(str_line)
    numbers_replaced = 0

    while numbers_replaced < numbers_found:
        index = None

        for key in numbers_map.keys():
            try:
                found_index = str_line.lower().index(key)
                if index is None or found_index < index: 
                    index = found_index
                    word = key[:-1]
                    number = numbers_map[key]
            except ValueError:
                continue
        
        str_line = str_line.replace(word, str(number), 1)
        numbers_replaced += 1

    return str_line

# format words in the string to numbers and combine the first digit and the last digit to form a single two-digit number and return the sum.
def part_two(lines):
    total = 0 
    for line in lines:
        formatted_str = replace_words_for_digits(line)
        number = find_first_number(formatted_str)
        number += find_last_number(formatted_str)
        total += int(number)
    return total 

my_text = read_file_return_list('text.txt')

answer_part_two = part_two(my_text)

print(f'The answer to part two is: {answer_part_two}')