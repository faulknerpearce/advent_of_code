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
    for row in range(start_row, end_row): # Iterate through the rows within the specified range
        for col in range(start_col, end_col): # Iterate through the columns within the specified range
            grid[row][col] = 1 # change this to be a state that will be passes to the function. 

def toggle_lights(start, end):
    pass

def follow_instructions():
    # check state (on, off, or toggle) and call the appropriate function (set lights or toggle_lights)
    pass

def read_instructions(instructions_list):
    for index in range(0, len(instructions_list), 5):
        state = instructions_list[index]
        the_start_row = instructions_list[index+1]
        the_start_col = instructions_list[index+2]
        the_end_row = instructions_list[index+3]
        the_end_col = instructions_list[index+4]
        
        print(f'Our instructions are. State: {state}. start row: {the_start_row}. start col: {the_start_col}. end row: {the_end_row}. end col: {the_end_col}.')
        # Call follow instructions. 

lights = create_grid(5, 5)

instructions = get_instructions()

read_instructions(instructions)








 