from machine import MachineConfig
from part_1 import read_file_return_2d_list, get_token_count

def part_two(instructions, num):
    '''Processes instructions to compute the total cost for each possible prize.'''
    total = 0 

    for instruction in instructions:

        claw_machine = MachineConfig(instruction[0], instruction[1], instruction[2], instruction[3],  num + instruction[4], num + instruction[5])
 
        total += get_token_count(claw_machine)

    return total

# Event: https://adventofcode.com/2024/day/13
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input, 10000000000000)

    print(f"The answer to part two is: {answer}")
