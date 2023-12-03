def read_file_to_list(file):
    with open(file) as text:
        text_lines = text.read().splitlines()
    return text_lines

def find_first_number(line):
    for index in range(len(line)):
        if ord(line[index]) >= 49 and ord(line[index]) <= 57:
            return line[index]
    return None 

def find_last_number(line):
    for index in range(1, len(line)+1):
        if ord(line[-index]) >= 49 and ord(line[-index]) <=57:
            return line[-index] 
    return None 

def part_one(lines):
    total = 0 
    for line in lines:
        numbers = find_first_number(line)
        numbers += find_last_number(line)
        total += int(numbers)

    return total 
 
my_text = read_file_to_list('text.txt')

answer_part_one = part_one(my_text)

print(f'The answer to part one is: {answer_part_one}')
