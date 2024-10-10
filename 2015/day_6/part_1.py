import re

# This will read and format a text file and return a 2d list of instructions.
def read_file_return_2d_list(file):
    with open(file) as text:
        formatted = re.sub(r'turn|through|,', ' ', text.read())

        return [ line.split() for line in formatted.split('\n') ]

# This will create a two-dimensional list.
def create_matrix(size):
    return [[ 0 for _ in range(size) ] for _ in range(size) ]

# Set the specified rectangular range of lights to the 'on' or 'off' state in the grid.
def set_lights(power, start_row, end_row, start_col, end_col, matrix):
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            matrix[row][col] = power

    return matrix

# Toggle the specified rectangular range of lights.
def toggle_lights(start_row, end_row, start_col, end_col, matrix):
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if matrix[row][col] == 1:
                matrix[row][col] = 0 
            else:
                matrix[row][col] = 1

    return matrix

# Count the number of lights that are turned on.
def count_lights(matrix):
    count = 0 

    for row in matrix:
        for col in row:
            count += col

    return count

# Follow the provided instructions and return the adjusted light grid.
def part_one(instructions, matrix):
    for instruction in instructions:
        if instruction[0] == 'on':
            matrix = set_lights(1, int(instruction[1]), int(instruction[3]), int(instruction[2]), int(instruction[4]), matrix)
        elif instruction[0] == 'off':
            matrix = set_lights(0, int(instruction[1]), int(instruction[3]), int(instruction[2]), int(instruction[4]), matrix)
        else: 
            matrix = toggle_lights(int(instruction[1]), int(instruction[3]), int(instruction[2]), int(instruction[4]), matrix)
       
    return matrix

if __name__ == "__main__":

    puzzle_input = read_file_return_2d_list('text.txt')

    matrix = create_matrix(1000)

    adjusted_matrix = part_one(puzzle_input, matrix)

    answer = count_lights(adjusted_matrix)

    print(f'The answer to part one is: {answer}')
