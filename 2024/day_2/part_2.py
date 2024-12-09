from part_1 import read_file_return_2d_list

# Determine whether the array trend is decreasing or increasing.
def get_trend(array):
    incr_count = 0
    decr_count = 0
    
    for i in range(1, len(array)):

        if array[i] > array[i-1]:
            incr_count += 1

        elif array[i] < array[i-1]:
            decr_count += 1
    
    return decr_count > incr_count

# Check if the array follows a valid trend (increasing or decreasing).
def has_valid_trend(array, desending):
    for i in range(1, len(array)):
        
        if desending:
            if array[i-1] < array[i]:
                return False
        else:
            if array[i-1] > array[i]:
                return False
            
    return True

# Verifies that the difference between the current number and its adjacent numbers are greater than 1 and less than 3.
def has_valid_delta(array):
    for i in range(1, len(array) - 1):
        left = abs(array[i] - array[i-1])
        right = abs(array[i] - array[i+1])

        if (left < 1 or left > 3) or (right < 1 or right > 3):
            return False

    return True

# Recursively determine if removing a single element from the array can result in a valid trend and delta differences.
def safe_with_one_removal(level, trend, original_level=None, tries=0):
    
    if tries == 0:
        new_level = level[tries+1:]
        if has_valid_trend(new_level, trend) and has_valid_delta(new_level):
            return True
        
        else:
            return safe_with_one_removal(new_level, trend, level, tries+1)
    
    elif tries < len(original_level):
        new_level = original_level[:tries] + original_level[tries+1:]

        if has_valid_trend(new_level, trend) and has_valid_delta(new_level):
            return True
        
        else:
            return safe_with_one_removal(new_level, trend, original_level, tries+1)

    else:
        return False

# Count the number of safe levels with or without one removal.    
def part_two(levels):
    count = 0

    for level in levels:

        level_trend = get_trend(level)

        if has_valid_trend(level, level_trend) and has_valid_delta(level):
            count += 1

        else:
            if safe_with_one_removal(level, level_trend):
                count += 1

    return count 

# Event: https://adventofcode.com/2024/day/2
if __name__ == '__main__': 

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')