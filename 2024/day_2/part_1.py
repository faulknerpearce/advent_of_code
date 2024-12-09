# Reads a file and returns its contents as a 2D list of integers.
def read_file_return_2d_list(file):
    with open(file) as data:
        array = [[int(num) for num in line.split()] for line in data.readlines()] 

    return array

# Verifies that the difference between the current number and its adjacent numbers are greater than 1 and less than 3.
def validate_adjacent_number_differences(array, index):
    difference_left = abs(array[index -1] - array[index])

    if index == len(array) -1:
        return difference_left >= 1 and difference_left <= 3
    
    else:
        difference_right = abs(array[index] - array[index +1])

        return difference_left >= 1 and difference_left <= 3 and difference_right >= 1 and difference_right <= 3

# Determines if a given array is "safe" based on decreasing/increasing sequence rules.
def is_safe(array):
    decreasing = array[0] > array[1]
    
    last_num = array[0]

    for i in range(1, len(array)):
        if (decreasing and array[i] < last_num) or (not decreasing and array[i] > last_num):
            if validate_adjacent_number_differences(array, i):
                last_num = array[i]
            else:
                return False
        else:
            return False

    return True

# Counts the number of "safe" levels in a list of arrays.
def part_one(levels):
    return sum(map(is_safe, levels))

# Event: https://adventofcode.com/2024/day/2
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
