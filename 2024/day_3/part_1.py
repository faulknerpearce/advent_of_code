import re 

# Reads a file and extracts valid 'mul(a,b)' instructions into a list of number pairs.
def read_file_return_list(file):
    with open(file) as text:

        valid_instructions = re.findall(r'mul\(\d+,\d+\)', text.read())
        
        array = [re.sub(r'mul|\(|\)', '', line).split(',') for line in valid_instructions]

    return array

# Computes the sum of the product of number pairs from the instructions.
def part_one(instructions):
    
    return sum(map(lambda instruction: int(instruction[0]) * int(instruction[1]), instructions))

# Event: https://adventofcode.com/2024/day/3
if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
