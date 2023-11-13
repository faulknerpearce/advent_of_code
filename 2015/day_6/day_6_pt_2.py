import re

def get_instructions():
    with open('text.txt', 'r') as text:
        my_string = text.read()
        cleaned_string = re.sub(r'\s+|,', ' ', my_string)  # Replace multiple spaces with a single space
        removed_words = re.sub(r'turn|through|', '', cleaned_string)  # Remove words (turn) and (through)
        instructions = removed_words.split()
        return instructions

# This will create a two-dimensional list.
def create_grid(length, height):
    grid = [[0 for i in range(length)] for j in range(height)]
    return grid

# Set the specified rectangular range of lights to the 'on' or 'off' state in the grid.
def set_lights_two(light_grid, start_row, start_col, end_row, end_col, power):
    if power == 'on':
        adjustment = 1
    else:
        adjustment = -1
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            light_grid[row][col] = max(light_grid[row][col] + adjustment, 0)
    return light_grid

def toggle_lights_two(light_grid, start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            light_grid[row][col] += 2
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
        power, the_start_row, the_start_col, the_end_row, the_end_col = instructions_list[i:i+5]

        if power == 'on' or power == 'off':
            light_grid = set_lights_two(light_grid, int(the_start_row), int(the_start_col), int(the_end_row), int(the_end_col), power)
            #print(f'{show_grid(light_grid)}\n')
        else:
            light_grid = toggle_lights_two(light_grid, int(the_start_row), int(the_start_col), int(the_end_row), int(the_end_col))
            #print(f'{show_grid(light_grid)}\n')
    return light_grid

# ________Main Program_________ #
instructions = get_instructions()

my_light_grid = create_grid(1000, 1000)

adjusted_lights = follow_instructions(instructions, my_light_grid)

print(count_lights(adjusted_lights))

