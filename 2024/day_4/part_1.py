# Reads a file and returns the content as a 2d array of strings.
def read_file_return_2d_list(file):
    with open(file) as data:
        array = [line.strip('\n') for line in data.readlines()]

    return array

# Checks if a string (or it's reverse) matches the target word.
def check_string(string):
    word = 'XMAS'
    
    return string == word or string[::-1] == word

# Searches for occurrences of the word horizontally in the array.
def search_horizontal(arrays):
    count = 0

    for array in arrays:
        for i in range(len(array) -3):
            word = array[i:i+4]

            if check_string(word):
                count += 1

    return count

# Searches for occurrences of the word vertically in the array.
def search_vertical(arrays):
    count = 0

    for row in range(len(arrays) -3):
        for col in range(len(arrays[row])):

            word = arrays[row][col] + arrays[row+1][col] + arrays[row+2][col] + arrays[row+3][col]

            if check_string(word):
                count += 1

    return count 

# Searches for occurrences of the word diagonally (both directions) in the array.
def search_diagonal(arrays):
    count = 0

    for row in range(len(arrays) -3):
        for col in range(len(arrays[row]) -3):

            diagonal_right = arrays[row][col] + arrays[row+1][col+1] + arrays[row+2][col+2] + arrays[row+3][col+3]
            diagonal_left = arrays[row][col+3] + arrays[row+1][col+2] + arrays[row+2][col+1] + arrays[row+3][col]

            if check_string(diagonal_right):
                count += 1

            if check_string(diagonal_left):
                count += 1

    return count

# Combines results from horizontal, vertical, and diagonal searches.
def part_one(arrays):

    horizontal = search_horizontal(arrays)

    vertical = search_vertical(arrays)

    diagonal = search_diagonal(arrays)

    return horizontal + vertical + diagonal

      
if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    answer = part_one(puzzle_input)

    print(f'The answer to part one is: {answer}')
