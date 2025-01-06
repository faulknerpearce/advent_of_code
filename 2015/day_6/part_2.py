from part_1 import read_file_return_2d_list, create_matrix, count_lights

def get_volts(power):
    '''Convert the power state to a corresponding voltage adjustment.'''
    volt = 1 if power == 'on' else -1
    return volt

def set_lights(power, start_row, end_row, start_col, end_col, matrix):
    '''Set the specified rectangular range of lights to the 'on' or 'off' state in the grid.'''
    volts = get_volts(power)
    
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col +1 ):
            matrix[row][col] = max(matrix[row][col] + volts, 0)
    
    return matrix

def toggle_lights(start_row, end_row, start_col, end_col, matrix):
    '''Toggle the state of lights in the specified area by adding 2 to their current state.'''
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            matrix[row][col] += 2
    
    return matrix

def part_two(instructions, matrix):
    '''Follow the provided instructions and return the adjusted light grid.'''
    for instruction in instructions:
        if instruction[0] == 'on' or instruction[0] == 'off':
            matrix = set_lights(instruction[0], int(instruction[1]), int(instruction[3]), int(instruction[2]), int(instruction[4]), matrix)
        else: 
            matrix = toggle_lights(int(instruction[1]), int(instruction[3]), int(instruction[2]), int(instruction[4]), matrix)

    return matrix

# Event: https://adventofcode.com/2015/day/6
if __name__ == "__main__":
    
    puzzle_input = read_file_return_2d_list('text.txt')

    matrix = create_matrix(1000)

    adjusted_matrix = part_two(puzzle_input, matrix)

    answer = count_lights(adjusted_matrix)

    print(f'The answer to part two is: {answer}')

