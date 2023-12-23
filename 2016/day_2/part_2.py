# Reads a file and returns an array of directions.
def read_file_return_list(file):
    with open(file) as data:
        array = [line for line in data.readlines()]
    return array

# Finds the current position's row and column index in a 2D array
def get_index(array, current_position):
    for row in range(len(array)):
        if current_position in array[row]:
            col_index = array[row].index(current_position)
            row_index = row
            break
    return row_index, col_index

# Determines the digit on the keypad after following a sequence of directions
def get_digit(line, array, position):
    
    row_index, col_index = get_index(array, position)

    for letter in line:
        if letter == 'U' and row_index > 0:
            row_index -= 1
        elif letter == 'D' and row_index < len(array) - 1:
            row_index += 1
        elif letter == 'L' and col_index > 0:
            col_index -= 1
        elif letter == 'R' and col_index < len(array[row_index]) - 1:
            col_index += 1

    return array[row_index][col_index]

# Calculates a sequence of digits based on the directions provided in each line
def get_digits(lines, array, value=5):
    digits = ''
    for line in lines:
       value = get_digit(line, array, value)
       digits += str(value)
    
    return digits

#________Main Program_________ # 
keypad_two = [[1], [2, 3, 4], [5, 6, 7, 8, 9], ['A', 'B', 'C'], ['D']]


my_input = read_file_return_list('text.txt')  

answer = get_digits(my_input, keypad_two)  

print(f'The answer to part one is: {answer}')
