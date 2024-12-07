from part_1 import read_file_return_2d_list

# Checks if a string (or it's reverse) matches the target word.
def check_string(string):
    word = 'MAS'
    
    return string == word or string[::-1] == word

# Searches for occurrences of the word diagonally (in both directions) creating a X in the 2D array.
def part_two(arrays):
    count = 0

    for row in range(len(arrays) -2):
        for col in range(len(arrays[row]) -2):

            diagonal_right = arrays[row][col] + arrays[row+1][col+1] + arrays[row+2][col+2]
            diagonal_left = arrays[row][col+2] + arrays[row+1][col+1] + arrays[row+2][col]

            if check_string(diagonal_right) and check_string(diagonal_left):
                count += 1

    return count

if __name__ == '__main__':
    
    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_two(puzzle_input)

    print(f'The answer to part two is: {answer}')
