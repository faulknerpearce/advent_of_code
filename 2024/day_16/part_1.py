import heapq

def read_file_return_2d_list(file):
    with open(file) as data:
        array = [list(line.strip('\n')) for line in data.readlines()]
        return array

def get_starting_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col


def is_valid(row, col, array, visited):
    return 0 <= row < len(array) and 0 <= col < len(array[0]) and array[row][col] != '#' and (row, col) not in visited

def breath_first_search(start_row, start_col, matrix):
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    directions_list = ['N', 'E', 'S', 'W']
    queue = [(0, start_row, start_col, 'E')]  
    visited = {}

    while queue:
        
        cur_score, cur_row, cur_col, cur_direction = heapq.heappop(queue)

        # Skip if this state has already been visited with a lower score
        if (cur_row, cur_col, cur_direction) in visited and visited[(cur_row, cur_col, cur_direction)] <= cur_score:
            continue

        # Mark the current state as visited with the current score
        visited[(cur_row, cur_col, cur_direction)] = cur_score

        # Check if the current cell is the end
        if matrix[cur_row][cur_col] == 'E':
            return cur_score

        # Forward Move: Move in the current direction
        new_row = cur_row + directions[cur_direction][0]
        new_col = cur_col + directions[cur_direction][1]

        if is_valid(new_row, new_col, matrix, visited):
            heapq.heappush(queue, (cur_score + 1, new_row, new_col, cur_direction))

        # Rotations: Consider valid rotations
        for direction in directions_list:
            if direction != cur_direction:
                # Check if moving in the rotated direction would be valid
                rotated_row = cur_row + directions[direction][0]
                rotated_col = cur_col + directions[direction][1]

                if is_valid(rotated_row, rotated_col, matrix, visited):
                    heapq.heappush(queue, (cur_score + 1000, cur_row, cur_col, direction))

if __name__ == '__main__':

    puzzle_input = read_file_return_2d_list('text.txt')

    starting_row, starting_col = get_starting_position(puzzle_input)

    answer = breath_first_search(starting_row, starting_col, puzzle_input)

    print(f'The answer to part one is: {answer}')