import re 

# Reads a file and returns a formatted two dimensional list. 
def read_file_return_2D_list(file):

    with open(file) as text:
        formatted_text = re.sub(r'|y|=|by|rotate|', '', text.read().replace('x', ' '))
        instructions = [line.split() for line in formatted_text.split('\n')]

    return instructions

# Generates a matrix with the specified length and height.
def generate_martix(width, height):
    matrix = [['.' for _ in range(width)] for _ in range(height)]

    return matrix

# Truns pixels on in the matrix up to the provided row and column.
def turn_on(end_col, end_row, matrix):
    for row in range(end_row):
        
        for col in range(end_col):
            matrix[row][col] = '#'

    return matrix

# Gets elements from the specified column in every row (Helper function for shift_column).
def get_pixels_from_column(col, matrix):
    column_pixels = []

    for row in matrix:
        column_pixels.append(row[col])
    
    return column_pixels
    
# Shifts pixels in a specific row of the matrix to the right by the specified amount.
def shift_accross(row, shift_amount, matrix):
    
    for _ in range(shift_amount):
        shifted = matrix[row][-1:] + matrix[row][:-1]
        matrix[row] = shifted

    return matrix

# Shifts pixels in a specific row of the matrix to the right by the specified amount.
def shift_down(col, shift_amount, matrix):

    for _ in range(shift_amount):
        pixels = get_pixels_from_column(col, matrix)
        shifted_pixels = pixels[-1:] + pixels[:-1]

        for i in range(len(matrix)):
            matrix[i][col] = shifted_pixels[i]

    return matrix 

# Processes a list of instructions to manipulate the pixels on a screen.
def adjust_pixels(instructions, matrix):

    for instruction in instructions:

        if instruction[0] == 'rect':
            matrix = turn_on(int(instruction[1]), int(instruction[2]), matrix)
        
        elif instruction[0] == 'column':
            matrix = shift_down(int(instruction[1]), int(instruction[2]), matrix)

        elif instruction[0] == 'row':
             matrix = shift_accross(int(instruction[1]), int(instruction[2]), matrix)

        else: 
            print('Instruction Read Error.')

    return matrix

# Returns the total amount of light pixels.
def part_one(matrix):
    total = 0

    for row in matrix:
        total += row.count('#')
        
    return total

# Event: https://adventofcode.com/2016/day/8
if __name__ == '__main__':

    puzzle_input = read_file_return_2D_list('text.txt')

    my_screen = generate_martix(50, 6)

    adjusted_screen = adjust_pixels(puzzle_input, my_screen)

    answer = part_one(adjusted_screen)

    print(f'The answer to part one is: {answer}')
