# Read the contents of a file and returns as a list of strings.
def read_file_return_list(file):
    with open(file) as text:
        text_lines = text.read().splitlines()
    
    return text_lines

# Find and return the first numeric character in a string.
def find_first_number(line):
    for index in range(len(line)):
        if ord(line[index]) >= 49 and ord(line[index]) <= 57:
            return line[index]
    
    return None 

# Find and return the last numeric character in a string.
def find_last_number(line):
    for index in range(1, len(line)+1):
        if ord(line[-index]) >= 49 and ord(line[-index]) <= 57:
            return line[-index] 
    
    return None 

# combine the first digit and the last digit to form a single two-digit number and return the sum.
def part_one(lines):
    total = 0 
    
    for line in lines:
        numbers = find_first_number(line)
        numbers += find_last_number(line)
        total += int(numbers)

    return total 

#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    answer_part_one = part_one(puzzle_input)

    print(f'The answer to part one is: {answer_part_one}')
