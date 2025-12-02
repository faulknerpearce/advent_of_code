# Parse the input file and return a list of instructions
def read_file_return_list(file):
    with open(file) as data:

        return data.read().split('\n')

# Rotate the dial position by the given amount in the specified direction   
def rotate(curent_position, amount, direction):

    if direction == 'R':
        return (curent_position + int(amount)) % 100
    
    else:
        return (curent_position - int(amount)) % 100

# Process instructions and count how many times the dial reaches position 0  
def part_one(instructions):
    count = 0
    dial_position = 50

    for instruction in instructions:
        dial_position = rotate(dial_position, instruction[1:], instruction[0])

        if dial_position == 0:
            count += 1

    return count
 
# Event: https://adventofcode.com/2025/day/1       
if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
