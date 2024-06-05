from part_1 import read_file_return_list, get_row_and_col_indexes, get_digits

# Finds the row and column indexes of the current digit in a 2D array.
def get_row_and_col_indexes(current_digit, array):
    for row in range(len(array)):
        if current_digit in array[row]:
            col =  array[row].index(current_digit)
            return row, col 

# Determines the digit on the keypad after following a sequence of directions.
def get_single_digit(current_digit, instruction, array):
    row_index, col_index = get_row_and_col_indexes(current_digit, array)
    
    for letter in instruction:
        if letter == 'U' and row_index > 0:
            if array[row_index -1][col_index] != 0:
                row_index -= 1 
          
        elif letter == 'D' and row_index < len(array) -1:
            if array[row_index +1][col_index] != 0:
                row_index += 1 
      
        elif letter == 'L' and col_index > 0:
            if array[row_index][col_index -1] != 0:
                col_index -= 1 
          
        elif letter == 'R' and col_index < len(array) -1:
            if array[row_index][col_index +1] != 0:
                col_index += 1   
        
    return array[row_index][col_index]

# Returns the resulting password after following the directions provided.
def get_digits(current_digit, instructions, array):
    digits = ''

    for instruction in instructions:
        current_digit = get_single_digit(current_digit, instruction, array)
        digits += str(current_digit)

    return digits

#________Main Program_________ # 
if __name__ == "__main__":
    
    keypad_two = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]

    puzzle_input = read_file_return_list('text.txt') 

    default_key = 5 

    answer = get_digits(default_key, puzzle_input, keypad_two)

    print(f'The answer to part one is: {answer}')
    