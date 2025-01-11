import heapq

def read_file_return_2d_list(file):
    '''Reads the input file and returns its content as a 2D matrix.'''
    with open(file) as data:
        return [list(line.strip('\n')) for line in data.readlines()]

def get_starting_position(matrix):
    '''Finds the initial position (x, y) of S in the matrix.'''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col

def is_valid_state(row, col, array):
    '''Checks if a position (row, col) is within the bounds of the array and not blocked by a wall.'''
    return 0 <= row < len(array) and 0 <= col < len(array[0]) and array[row][col] != '#'

def eligible_position(score, row, col, direction, visited):
    '''Determines if a state (row, col, direction) is worth adding to the queue based on score.'''
    return (row, col, direction) not in visited or score < visited[(row, col, direction)]

def breath_first_search(start_row, start_col, matrix):
    '''Uses BFS with a priority queue to find the minimum score path from 'S' to 'E'.'''
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    queue = [(0, start_row, start_col, 'E')]  
    visited = {}

    while queue:
        cur_score, cur_row, cur_col, cur_direction = heapq.heappop(queue)

        if matrix[cur_row][cur_col] == 'E':
            return cur_score

        new_row = cur_row + directions[cur_direction][0]
        new_col = cur_col + directions[cur_direction][1]

        if is_valid_state(new_row, new_col, matrix) and eligible_position(cur_score + 1, new_row, new_col, cur_direction, visited):
            visited[(new_row, new_col, cur_direction)] = cur_score + 1
            heapq.heappush(queue, (cur_score + 1, new_row, new_col, cur_direction))

        for direction in directions.keys():
            if direction != cur_direction and eligible_position(cur_score + 1000, cur_row, cur_col, direction, visited):
                visited[(cur_row, cur_col, direction)] = cur_score + 1000
                heapq.heappush(queue, (cur_score + 1000, cur_row, cur_col, direction))

    return None

# Event: https://adventofcode.com/2024/day/16
if __name__ == '__main__':
    puzzle_input = read_file_return_2d_list('text.txt')

    starting_row, starting_col = get_starting_position(puzzle_input)

    answer = breath_first_search(starting_row, starting_col, puzzle_input)

    print(f'The answer to part one is: {answer}')