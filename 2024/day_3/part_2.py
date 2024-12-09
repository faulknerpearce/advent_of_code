import re

# Reads a file and extracts 'mul(a,b)', 'do()', and 'don't()' instructions as arrays
def read_file_return_list(file):
    with open(file) as text:

        valid_instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', text.read())
        
        array = [re.sub(r'mul|\(|\)|\'', '', line).split(',') for line in valid_instructions]

    return array

# Processes instructions and calculates the total based on enable/disable commands.
def part_two(instructions):
    enable_mul = True
    total = 0

    for instruction in instructions:

        if instruction[0].isdigit() and enable_mul:  
            product = int(instruction[0]) * int(instruction[1])
            total += product

        elif instruction[0] == 'dont':
            enable_mul = False

        elif instruction[0] == 'do':
            enable_mul = True

    return total

# Event: https://adventofcode.com/2024/day/3
if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')
