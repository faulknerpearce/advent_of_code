from part_1 import read_file_return_list

# Finds the current position's row and column index in a 2D array
def get_row_col_index(array, current_character):
    for row in range(len(array)):
        if current_character in array[row]:
            col_index = array[row].index(current_character)
            row_index = row
            break
    return row_index, col_index

# Determines the digit on the keypad after following a sequence of directions
def part_two(line, array, position):
    max_index = len(array) - 1
    row_index, col_index = get_row_col_index(array, position)
    
    for letter in line:
        if letter == 'U' and row_index > 0:
            check_row = row_index - 1
            if array[check_row][col_index] != 0:
                row_index -= 1 
          
        elif letter == 'D' and row_index < max_index:
            check_row = row_index + 1
            if array[check_row][col_index] != 0:
                row_index += 1 
      
        elif letter == 'L' and col_index > 0:
            check_col = col_index - 1
            if array[row_index][check_col] != 0:
                col_index -= 1 
          
        elif letter == 'R' and col_index < max_index:
            check_col = col_index + 1
            if array[row_index][check_col] != 0:
                col_index += 1   
        
    return array[row_index][col_index]

# Calculates a sequence of digits based on the directions provided in each line
def get_characters(lines, array, value=5):
    digits = ''
    for line in lines:
       value = part_two(line, array, value)
       digits += str(value)
    
    return digits

#________Main Program_________ # 
if __name__ == "__main__":
    
    keypad_two = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]

    puzzle_input = read_file_return_list('text.txt')  

    answer = get_characters(puzzle_input, keypad_two)  

    print(f'The answer to part one is: {answer}')

