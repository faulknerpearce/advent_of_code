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

# Checks if the remaining length of the string is sufficient for the decompression process.
def has_sufficient_length(length_required, right_edge, the_string):
    remaining_length = len(the_string) - (right_edge + 1)

    if remaining_length == 0:
        return False
    else:
        return int(length_required) <= int(remaining_length)

# Generates a string by repeating a specified segment of the provided string.
def get_repeating_characters(the_string, marker_right_edge, required_length, amount):
    repeating = ''
    for _ in range(amount):
        repeating += (the_string[marker_right_edge + 1:marker_right_edge+required_length + 1])

    return repeating

# Decompresses a string according to markers that define how to expand certain segments. 
def decompress_string(the_string):
    decompressed_str = ''
    current_index = 0

    while current_index < len(the_string):
        
        if has_marker(the_string[current_index:]):
            
            marker_left_edge, marker_right_edge = get_marker_indices(the_string, current_index)
            decompressed_str += (the_string[current_index:marker_left_edge])
            marker = the_string[marker_left_edge:marker_right_edge + 1]
            pattern_length, increase_by = unpack_marker(marker)

            if has_sufficient_length(pattern_length, marker_right_edge, the_string):
                
                decompressed_characters = get_repeating_characters(the_string, marker_right_edge, pattern_length, increase_by)
                decompressed_str += (decompressed_characters)
                current_index = marker_right_edge + pattern_length + 1
            else:
                current_index = marker_right_edge + 1
        else:
            decompressed_str += the_string[current_index:]
            break

    return decompressed_str

# Calculates the total length of decompressed strings from an array of strings 
def part_one(string):
    decompressed_length = 0
    
    decompressed_string = decompress_string(string)

    decompressed_length += len(decompressed_string)

    return decompressed_length

#________Main Program_________ # 
if __name__ == "__main__":
    
    puzzle_input = read_file_return_string('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
   
