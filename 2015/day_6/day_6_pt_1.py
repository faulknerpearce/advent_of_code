import re

def get_instructions():
    '''This will read and format a text file and return a list of instructions.'''
    with open('text.txt', encoding='utf-8') as text:
        my_string = text.read()
        cleaned_string = re.sub(r'\s+|,', ' ', my_string)
        removed_words = re.sub(r'turn|through|', '', cleaned_string)
        instructions = removed_words.split()
        return instructions

def create_grid(length, height):
    '''This will create a two-dimensional list.'''
    grid = [[0 for i in range(length)] for j in range(height)]
    return grid

def set_lights(light_grid, start_row, start_col, end_row, end_col, power):
    '''Set the specified rectangular range of lights to the 'on' or 'off' state in the grid.'''
    if power == 'on':
        adjustment  = 1
    else:
        adjustment = 0
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            light_grid[row][col] = adjustment
    return light_grid

def toggle_lights(light_grid, start_row, start_col, end_row, end_col):
    '''Toggle the specified rectangular range of lights.'''
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if light_grid[row][col] == 0:
                light_grid[row][col] = 1
            else:
                light_grid[row][col] = 0
    return light_grid

def count_lights(light_grid):
    '''Count the number of lights that are turned on.'''
    result = 0
    for row in light_grid:
        for num in row:
            result += num
    return result

def follow_instructions(instructions_list, light_grid):
    '''Follow the provided instructions and return the adjusted light grid.'''
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

my_instructions = get_instructions()

my_light_grid = create_grid(1000, 1000)

adjusted_lights = follow_instructions(my_instructions, my_light_grid)

print(count_lights(adjusted_lights))
