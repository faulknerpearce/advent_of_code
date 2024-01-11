import re

# Reads from a file and returns its content as a list of stripped lines.
def read_file_return_list(file):
    with open(file) as data:
        lines = [line.strip() for line in data.readlines()]
    return lines

# Returns true if a marker contains an opened and closed parenthesis in that order.
def has_marker(arr):
   return bool(re.search(r'\([^\)]+\)', arr))

# Returns the indices of the opening and closing parentheses of the first marker in the string.
def get_marker_indices(arr, start=0):
    found_left = False

    for i in range(start, len(arr)): 
        if arr[i] == '(':
            found_left = True
            start_idx = i

        elif arr[i] == ')' and found_left:
            end_idx = i
            break

    return start_idx, end_idx

# Returns the length of the pattern and the number of times it should be repeated.
def unpack_marker(marker):
    values = re.findall(r'\d+', marker)
    
    return int(values[0]), int(values[1])

# Checks if the remaining length of the string is sufficient for the decompression process.
def has_sufficient_length(length_required, right_edge, arr):
    remaining_length = len(arr) - (right_edge + 1)

    if remaining_length == 0:
        return False
    else:
        return int(length_required) <= int(remaining_length)

# Generates a string by repeating a specified segment of the provided string.
def get_repeating_characters(line, marker_right_edge, required_length, amount):
    repeating = ''
    for _ in range(amount):
        repeating += (line[marker_right_edge + 1:marker_right_edge+required_length + 1])

    return repeating

# Decompresses a string according to markers that define how to expand certain segments. 
def decompress_string(arr):
    decompressed_str = ''
    current_index = 0

    while current_index < len(arr):
        
        if has_marker(arr[current_index:]):
            
            marker_left_edge, marker_right_edge = get_marker_indices(arr, current_index)
            decompressed_str += (arr[current_index:marker_left_edge])
            marker = arr[marker_left_edge:marker_right_edge + 1]
            pattern_length, increase_by = unpack_marker(marker)

            if has_sufficient_length(pattern_length, marker_right_edge, arr):
                
                decompressed_characters = get_repeating_characters(arr, marker_right_edge, pattern_length, increase_by)
                decompressed_str += (decompressed_characters)
                current_index = marker_right_edge + pattern_length + 1
            else:
                current_index = marker_right_edge + 1
        else:
            decompressed_str += arr[current_index:]
            break

    return decompressed_str

# Calculates the total length of decompressed strings from an array of strings 
def part_one(lines):
    decompressed_length = 0
    
    for line in lines:
        decompressed_string = decompress_string(line)

        decompressed_length += len(decompressed_string)

    return decompressed_length

#________Main Program_________ # 
if __name__ == "__main__":
    
    puzzle_input = read_file_return_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
   
