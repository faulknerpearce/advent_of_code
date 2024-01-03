import re

# This will read and format a text file and return a list of instructions.
def read_file_return_list(file):
    with open(file, encoding='utf-8') as text:
        my_string = text.read()
        cleaned_string = re.sub(r'\s+|,', ' ', my_string)
        removed_words = re.sub(r'turn|through|', '', cleaned_string)
        instructions = removed_words.split()
        return instructions

# This will create a two-dimensional list.
def create_matrix(length, height):
    matrix = [[0 for _ in range(length)] for _ in range(height)]
    return matrix

# Set the specified rectangular range of lights to the 'on' or 'off' state in the grid.
def set_lights(light_grid, start_row, start_col, end_row, end_col, power):
    if power == 'on':
        adjustment  = 1
    else:
        adjustment = 0
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            light_grid[row][col] = adjustment
    return light_grid

# Toggle the specified rectangular range of lights.
def toggle_lights(light_grid, start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if light_grid[row][col] == 0:
                light_grid[row][col] = 1
            else:
                light_grid[row][col] = 0
    return light_grid

# Count the number of lights that are turned on.
def count_lights(light_grid):
    result = 0
    for row in light_grid:
        for num in row:
            result += num
    return result

# Follow the provided instructions and return the adjusted light grid.
def follow_instructions(instructions_list, light_grid):
    for i in range(0, len(instructions_list), 5):
        power, the_start_row, the_start_col, the_end_row, the_end_col = instructions_list[
            i:i+5]

        if power == 'on' or power == 'off':
            light_grid = set_lights(light_grid, int(the_start_row), int(
                the_start_col), int(the_end_row), int(the_end_col), power)
    
        else:
            light_grid = toggle_lights(light_grid, int(the_start_row), int(
                the_start_col), int(the_end_row), int(the_end_col))
            
    return light_grid

#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    my_light_grid = create_matrix(1000, 1000)

    adjusted_lights = follow_instructions(puzzle_input, my_light_grid)

    answer = count_lights(adjusted_lights)

    print(f'The answer to part one is: {answer}')
