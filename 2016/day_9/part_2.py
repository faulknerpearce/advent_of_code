import re

# Reads from a file and returns its content as a string.
def read_file_return_string(file):
    with open(file) as data:
        the_string = data.read()
    
    return the_string

# Returns true if a marker contains an opened and closed parenthesis in that order.
def has_marker(the_string):
   return bool(re.search(r'\([^\)]+\)', the_string))

# Returns the indices of the opening and closing parentheses of the first marker in the string.
def get_marker_indices(the_string, start=0):
    found_left = False

    for i in range(start, len(the_string)): 
        if the_string[i] == '(':
            found_left = True
            start_idx = i

        elif the_string[i] == ')' and found_left:
            end_idx = i
            break

    return start_idx, end_idx

# Returns the length of the pattern and the number of times it should be repeated.
def unpack_marker(marker):
    values = re.findall(r'\d+', marker)
    
    return int(values[0]), int(values[1])

# Generates a string by repeating a specified segment of the provided string.
def get_repeating_characters(the_string, marker_right_edge, required_length, amount):
    repeating = ''
    for _ in range(amount):
        repeating += (the_string[marker_right_edge + 1:marker_right_edge+required_length + 1])

    return repeating

# Calculates the total decompressed length of a string, including nested markers.
def calculate_decompressed_length(the_string, start_index=0):
    length = 0
    current_index = start_index

    while current_index < len(the_string):
        
        if has_marker(the_string[current_index:]):
            
            marker_left_edge, marker_right_edge = get_marker_indices(the_string, current_index)
            pattern_length, increase_by = unpack_marker(the_string[marker_left_edge:marker_right_edge + 1])

            nested_string_start = marker_right_edge + 1
            nested_string_end = nested_string_start + pattern_length
            
            nested_length = calculate_decompressed_length(the_string[nested_string_start:nested_string_end])

            length += (marker_left_edge - current_index) + nested_length * increase_by
            
            current_index = nested_string_end
        
        else:
            length += len(the_string) - current_index
            break

    return length

# Event: https://adventofcode.com/2016/day/9
if __name__ == "__main__":
    
    puzzle_input = read_file_return_string('text.txt')
    
    answer = calculate_decompressed_length(puzzle_input)
    
    print(f"The decompressed length of the file is: {answer}")
