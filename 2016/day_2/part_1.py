def read_file_return_list(file):
    '''Reads a file and returns an array of directions.'''
    with open(file) as text:
        string = [line.strip('\n') for line in text.readlines()]

    return string

# Finds the row and column indexes of the current digit in a 2D array.
def get_row_and_col_indexes(current_digit, array):
    for row in range(len(array)):
        if current_digit in array[row]:
            col =  array[row].index(current_digit)
            return row, col 

# Returns the final digit on the keypad after following a sequence of directions.         
def get_single_digit(current_digit, instruction, array):
    row_index, col_index = get_row_and_col_indexes(current_digit, array)

    for letter in instruction:

        if letter == 'U' and row_index > 0:  
            row_index -= 1
        
        elif letter == 'D' and row_index < len(array) -1:  
            row_index += 1    
        
        elif letter == 'R' and col_index < len(array) -1:  
            col_index += 1
        
        elif letter == 'L' and col_index > 0:  
            col_index -= 1

    return array[row_index][col_index]

# Returns the resulting password after following the directions provided.
def get_digits(current_digit, instructions, array):
    digits = ''

    for instruction in instructions:
        current_digit = get_single_digit(current_digit, instruction, array)
        digits += str(current_digit)

    return digits

# Event: https://adventofcode.com/2016/day/2
if __name__ == '__main__':

    puzzle_input = read_file_return_list('text.txt')

    keypad_one = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

    default_digit = 5
    
    answer = get_digits(default_digit, puzzle_input, keypad_one)

    print(f'The answer for part one is: {answer}')
    