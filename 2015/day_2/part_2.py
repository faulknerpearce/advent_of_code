from part_1 import read_file_return_2d_list 

def calculate_ribbon(length, width, height):
    '''Calculates the total ribbon needed for a single box, including the bow length.'''
    
    numbers = [length, width, height]
    numbers.remove(max(numbers))

    bow = length * width * height
    ribbon = numbers[0] * 2 + numbers[1] * 2

    return ribbon + bow

def calculate_total_ribbon(instructions):
    '''Calculates the total ribbon required for all boxes based on the instructions.'''
    total = 0

    for instruction in instructions:
        total += calculate_ribbon(int(instruction[0]), int(instruction[1]), int(instruction[2]))

    return total

# Event: https://adventofcode.com/2015/day/2
if __name__ == '__main__':
    
    puzzle_input = read_file_return_2d_list('text.txt')

    answer = calculate_total_ribbon(puzzle_input)

    print(f'The answer to part two is: {answer}')