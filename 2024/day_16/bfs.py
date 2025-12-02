def read_file_return_2d_list(file):
    with open(file) as data:
        array = [list(line.strip('\n')) for line in data.readlines()]

        return array
    
def get_starting_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col 
    
def is_valid(row, col, array, set):
    return array[row][col] != '#' and (row, col) not in set

def breath_first_search(start_row, start_col, matrix):
    directions = [[-1, 0], [0, 1], [1, 0],[0, -1]]
    queue = [(start_row, start_col)]
    visited = set()

    while queue:
        cur_row, cur_col = queue.pop(0)

        visited.add((cur_row, cur_col))

        if matrix[cur_row][cur_col] == 'E':
            print('end was found')

        for i in range(len(directions)):
            row = cur_row + directions[i][0]
            col = cur_col + directions[i][1]

            if is_valid(row, col, matrix, visited):
                queue.append((row, col))
                visited.add((row, col))

if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('/Users/austinfaulkner-pearce/workspace/advent_of_code/2024/day_16/test.txt')

    starting_row, starting_col = get_starting_position(puzzle_input)

    breath_first_search(starting_row, starting_col, puzzle_input)