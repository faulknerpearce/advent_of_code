# to do: 

import re

def get_instructions():
    with open('text.txt', 'r') as text:
        my_string = text.read()
        cleaned_string = re.sub(r'\s+|,', ' ', my_string)  # Replace multiple spaces with a single space
        removed_words = re.sub(r'turn|through|', '', cleaned_string)  # Remove 'turn', 'through'
        instructions = removed_words.split()
        return instructions

# This will create a two dimensional list.
def create_grid(length, height):
    grid = [[0 for i in range(length)] for i in range(height)]
    return grid 

# Set the specified rectangular range of lights to the 'on' state in the grid.
def set_lights(grid, start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            grid[row][col] = 1 # 0 or 1

def toggle_lights(start, end):
    pass

def read_instructions(instructions_list):
    for index in range(0, len(instructions_list), 5):
        state = instructions_list[index]
        the_start_row = instructions_list[index+1]
        the_start_col = instructions_list[index+2]
        the_end_row = instructions_list[index+3]
        the_end_col = instructions_list[index+4]
        print(f'Our instructions are. State: {state}. start row: {the_start_row}. start col: {the_start_col}. end row: {the_end_row}. end col: {the_end_col}.')

def show_nicole_grid(lights):
    for row in lights:
        print(row)

test = ['on', '887', '9', '959', '629', 'on', '454', '398', '844', '448', 'off', '539', '243', '559', '965', 'off', '370', '819', '676', '868']

lights = create_grid(5, 5)

set_lights(lights, 1, 0, 2, 3) # Will set the lights to [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

show_nicole_grid(lights)



#instructions = get_instructions()

#follow_instructions(instructions)
